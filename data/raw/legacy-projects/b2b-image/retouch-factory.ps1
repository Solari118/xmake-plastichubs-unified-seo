param(
    [string]$OutputDir = "C:\Users\Lostk\Documents\B2B机加工生图\output\factory-retouched"
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

if (-not ("FactoryPhotoProcessor" -as [type])) {
    Add-Type -ReferencedAssemblies System.Drawing -TypeDefinition @"
using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

public static class FactoryPhotoProcessor
{
    private static void ApplyOrientation(Image image)
    {
        const int OrientationId = 0x0112;
        try
        {
            if (Array.IndexOf(image.PropertyIdList, OrientationId) < 0) return;
            int orientation = image.GetPropertyItem(OrientationId).Value[0];
            switch (orientation)
            {
                case 2: image.RotateFlip(RotateFlipType.RotateNoneFlipX); break;
                case 3: image.RotateFlip(RotateFlipType.Rotate180FlipNone); break;
                case 4: image.RotateFlip(RotateFlipType.Rotate180FlipX); break;
                case 5: image.RotateFlip(RotateFlipType.Rotate90FlipX); break;
                case 6: image.RotateFlip(RotateFlipType.Rotate90FlipNone); break;
                case 7: image.RotateFlip(RotateFlipType.Rotate270FlipX); break;
                case 8: image.RotateFlip(RotateFlipType.Rotate270FlipNone); break;
            }
        }
        catch { }
    }

    private static RectangleF CoverCrop(int sourceWidth, int sourceHeight, int targetWidth, int targetHeight, float anchorX, float anchorY)
    {
        float sourceAspect = (float)sourceWidth / sourceHeight;
        float targetAspect = (float)targetWidth / targetHeight;
        if (sourceAspect > targetAspect)
        {
            float cropWidth = sourceHeight * targetAspect;
            float x = (sourceWidth - cropWidth) * Math.Max(0f, Math.Min(1f, anchorX));
            return new RectangleF(x, 0, cropWidth, sourceHeight);
        }
        else
        {
            float cropHeight = sourceWidth / targetAspect;
            float y = (sourceHeight - cropHeight) * Math.Max(0f, Math.Min(1f, anchorY));
            return new RectangleF(0, y, sourceWidth, cropHeight);
        }
    }

    private static Bitmap RenderPass(Image source, int width, int height, RectangleF sourceRect, ImageAttributes attributes)
    {
        Bitmap result = new Bitmap(width, height, PixelFormat.Format24bppRgb);
        result.SetResolution(96, 96);
        using (Graphics graphics = Graphics.FromImage(result))
        {
            graphics.Clear(Color.FromArgb(235, 238, 240));
            graphics.CompositingMode = CompositingMode.SourceCopy;
            graphics.CompositingQuality = CompositingQuality.HighQuality;
            graphics.InterpolationMode = InterpolationMode.HighQualityBicubic;
            graphics.PixelOffsetMode = PixelOffsetMode.HighQuality;
            graphics.SmoothingMode = SmoothingMode.HighQuality;
            graphics.DrawImage(source, new Rectangle(0, 0, width, height), sourceRect.X, sourceRect.Y, sourceRect.Width, sourceRect.Height, GraphicsUnit.Pixel, attributes);
        }
        return result;
    }

    private static Bitmap Sharpen(Bitmap source, float amount)
    {
        if (amount <= 0) return (Bitmap)source.Clone();
        Bitmap result = new Bitmap(source.Width, source.Height, PixelFormat.Format24bppRgb);
        Rectangle rect = new Rectangle(0, 0, source.Width, source.Height);
        BitmapData srcData = source.LockBits(rect, ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
        BitmapData dstData = result.LockBits(rect, ImageLockMode.WriteOnly, PixelFormat.Format24bppRgb);
        int bytes = Math.Abs(srcData.Stride) * source.Height;
        byte[] src = new byte[bytes];
        byte[] dst = new byte[bytes];
        Marshal.Copy(srcData.Scan0, src, 0, bytes);
        Array.Copy(src, dst, bytes);
        int stride = srcData.Stride;
        for (int y = 1; y < source.Height - 1; y++)
        {
            for (int x = 1; x < source.Width - 1; x++)
            {
                int i = y * stride + x * 3;
                for (int c = 0; c < 3; c++)
                {
                    float center = src[i + c];
                    float neighbors = src[i - stride + c] + src[i + stride + c] + src[i - 3 + c] + src[i + 3 + c];
                    int value = (int)Math.Round(center * (1f + 4f * amount) - neighbors * amount);
                    dst[i + c] = (byte)Math.Max(0, Math.Min(255, value));
                }
            }
        }
        Marshal.Copy(dst, 0, dstData.Scan0, bytes);
        source.UnlockBits(srcData);
        result.UnlockBits(dstData);
        return result;
    }

    public static void Process(string input, string output, int width, int height, float anchorX, float anchorY,
        float saturation, float contrast, float brightness, float red, float green, float blue, float gamma, float sharpen)
    {
        using (Image loaded = Image.FromFile(input))
        {
            ApplyOrientation(loaded);
            RectangleF crop = CoverCrop(loaded.Width, loaded.Height, width, height, anchorX, anchorY);

            float inv = 1f - saturation;
            float lr = 0.213f * inv;
            float lg = 0.715f * inv;
            float lb = 0.072f * inv;
            ColorMatrix saturationMatrix = new ColorMatrix(new float[][] {
                new float[] { lr + saturation, lr, lr, 0, 0 },
                new float[] { lg, lg + saturation, lg, 0, 0 },
                new float[] { lb, lb, lb + saturation, 0, 0 },
                new float[] { 0, 0, 0, 1, 0 },
                new float[] { 0, 0, 0, 0, 1 }
            });

            using (ImageAttributes saturationAttributes = new ImageAttributes())
            {
                saturationAttributes.SetColorMatrix(saturationMatrix);
                using (Bitmap baseImage = RenderPass(loaded, width, height, crop, saturationAttributes))
                {
                    float offset = 0.5f * (1f - contrast) + brightness;
                    ColorMatrix toneMatrix = new ColorMatrix(new float[][] {
                        new float[] { contrast * red, 0, 0, 0, 0 },
                        new float[] { 0, contrast * green, 0, 0, 0 },
                        new float[] { 0, 0, contrast * blue, 0, 0 },
                        new float[] { 0, 0, 0, 1, 0 },
                        new float[] { offset, offset, offset, 0, 1 }
                    });
                    using (ImageAttributes toneAttributes = new ImageAttributes())
                    {
                        toneAttributes.SetColorMatrix(toneMatrix);
                        toneAttributes.SetGamma(gamma);
                        using (Bitmap toned = RenderPass(baseImage, width, height, new RectangleF(0, 0, width, height), toneAttributes))
                        using (Bitmap finalImage = Sharpen(toned, sharpen))
                        {
                            ImageCodecInfo codec = null;
                            foreach (ImageCodecInfo item in ImageCodecInfo.GetImageEncoders())
                                if (item.FormatID == ImageFormat.Jpeg.Guid) codec = item;
                            using (EncoderParameters parameters = new EncoderParameters(1))
                            {
                                parameters.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, 94L);
                                finalImage.Save(output, codec, parameters);
                            }
                        }
                    }
                }
            }
        }
    }
}
"@
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$jobs = @(
    @{ In = "C:\Users\Lostk\AppData\Local\Temp\codex-clipboard-27e82df8-a044-4047-a2f9-fc893f78e2a4.png"; Out = "01-swiss-lathe-retouched.jpg"; AX=.50; AY=.50; Sat=.88; Con=1.08; Bri=.015; R=.98; G=.99; B=1.03; Gam=.96; Sharp=.10 },
    @{ In = "C:\Users\Lostk\AppData\Local\Temp\codex-clipboard-17fb23c9-c505-4c6a-ae2f-4e2396a3a0e9.png"; Out = "02-cnc-lathe-retouched.jpg"; AX=.50; AY=.50; Sat=.86; Con=1.08; Bri=.018; R=.98; G=.99; B=1.03; Gam=.95; Sharp=.10 },
    @{ In = "C:\Users\Lostk\Documents\WXWork\1688857103865500\Cache\Image\2026-07\ce8e5712-a360-46ad-abe3-649a85e92a7e.jpg"; Out = "03-print-farm-retouched.jpg"; AX=.50; AY=.34; Sat=.82; Con=1.07; Bri=.010; R=.98; G=.99; B=1.03; Gam=.98; Sharp=.09 },
    @{ In = "C:\Users\Lostk\Documents\WXWork\1688857103865500\Cache\Image\2026-07\39f70cec-32d9-4216-bd77-e92fd5141600.jpg"; Out = "04-machine-aisle-retouched.jpg"; AX=.50; AY=.42; Sat=.70; Con=1.13; Bri=.045; R=.96; G=.99; B=1.06; Gam=.68; Sharp=.10 },
    @{ In = "C:\Users\Lostk\AppData\Local\Temp\codex-clipboard-01572c09-fd0d-4996-8c7d-1caf9ca03caa.png"; Out = "05-cnc-workshop-retouched.jpg"; AX=.50; AY=.50; Sat=.84; Con=1.09; Bri=.020; R=.98; G=.99; B=1.03; Gam=.94; Sharp=.10 },
    @{ In = "C:\Users\Lostk\Documents\B2B机加工生图\input\factory-retouch\06-target-tight.png"; Out = "06-factory-visit-retouched.jpg"; AX=.50; AY=.50; Sat=.78; Con=1.10; Bri=.025; R=.98; G=.99; B=1.03; Gam=.90; Sharp=.10 },
    @{ In = "C:\Users\Lostk\AppData\Local\Temp\codex-clipboard-bfc130c2-6388-444f-be33-df2ffc8accb9.png"; Out = "07-bar-feeder-retouched.jpg"; AX=.50; AY=.50; Sat=.86; Con=1.08; Bri=.018; R=.98; G=.99; B=1.03; Gam=.95; Sharp=.10 },
    @{ In = "C:\Users\Lostk\AppData\Local\Temp\企业微信截图_17839952626402.png"; Out = "08-automated-line-retouched.jpg"; AX=.55; AY=.50; Sat=.82; Con=1.08; Bri=.015; R=.98; G=.99; B=1.03; Gam=.94; Sharp=.10 }
)

foreach ($job in $jobs) {
    $destination = Join-Path $OutputDir $job.Out
    [FactoryPhotoProcessor]::Process($job.In, $destination, 1000, 750, $job.AX, $job.AY, $job.Sat, $job.Con, $job.Bri, $job.R, $job.G, $job.B, $job.Gam, $job.Sharp)
    Write-Output $destination
}

$contactSheetPath = Join-Path $OutputDir "contact-sheet.jpg"
$contactSheet = New-Object System.Drawing.Bitmap 2000, 750
$contactSheet.SetResolution(96, 96)
$graphics = [System.Drawing.Graphics]::FromImage($contactSheet)
$graphics.Clear([System.Drawing.Color]::FromArgb(28, 32, 36))
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
try {
    for ($index = 0; $index -lt $jobs.Count; $index++) {
        $imagePath = Join-Path $OutputDir $jobs[$index].Out
        $image = [System.Drawing.Image]::FromFile($imagePath)
        try {
            $x = ($index % 4) * 500
            $y = [Math]::Floor($index / 4) * 375
            $graphics.DrawImage($image, $x, $y, 500, 375)
        } finally {
            $image.Dispose()
        }
    }
} finally {
    $graphics.Dispose()
}
$contactSheet.Save($contactSheetPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
$contactSheet.Dispose()
Write-Output $contactSheetPath
