param(
    [string]$SourcePath = "C:\Users\Lostk\Documents\B2B机加工生图\input\factory-retouch\06-people-locked-target.png",
    [string]$Output = "C:\Users\Lostk\Documents\B2B机加工生图\output\people-preserved-composite\factory-people-preserved-clean-v2.png"
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$source = [System.Drawing.Image]::FromFile($SourcePath)
$base = New-Object System.Drawing.Bitmap 1000,750
$g = [System.Drawing.Graphics]::FromImage($base)
$g.DrawImage($source,0,0,1000,750)
$source.Dispose()
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality

# Clean enclosed tooling cabinet between the two visitors. This region does not overlap either person.
$shadow = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(55,0,0,0))
$g.FillRectangle($shadow,238,250,202,500)
$shadow.Dispose()
$cabinetRect = New-Object System.Drawing.Rectangle 246,242,188,508
$cabinetBrush = New-Object System.Drawing.Drawing2D.LinearGradientBrush $cabinetRect,([System.Drawing.Color]::FromArgb(104,111,116)),([System.Drawing.Color]::FromArgb(61,68,73)),90
$g.FillRectangle($cabinetBrush,$cabinetRect)
$cabinetBrush.Dispose()
$framePen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(38,44,48)),5
$g.DrawRectangle($framePen,246,242,188,508)
$framePen.Dispose()
$seamPen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(145,151,154)),1
$g.DrawLine($seamPen,340,249,340,743)
$g.DrawLine($seamPen,252,520,428,520)
$seamPen.Dispose()
$handleBrush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(190,198,202))
$g.FillRectangle($handleBrush,324,465,9,42)
$g.FillRectangle($handleBrush,347,465,9,42)
$handleBrush.Dispose()

# Organized tooling cabinet on the right, replacing loose foam and offcuts outside the people silhouettes.
$rightRect = New-Object System.Drawing.Rectangle 815,548,185,202
$rightBrush = New-Object System.Drawing.Drawing2D.LinearGradientBrush $rightRect,([System.Drawing.Color]::FromArgb(77,92,86)),([System.Drawing.Color]::FromArgb(45,57,54)),90
$g.FillRectangle($rightBrush,$rightRect)
$rightBrush.Dispose()
$rightFrame = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(31,40,38)),4
$g.DrawRectangle($rightFrame,815,548,185,202)
$g.DrawLine($rightFrame,815,615,1000,615)
$g.DrawLine($rightFrame,815,682,1000,682)
$rightFrame.Dispose()
$labelBrush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(165,174,170))
$g.FillRectangle($labelBrush,965,575,12,28)
$g.FillRectangle($labelBrush,965,642,12,28)
$labelBrush.Dispose()

# Clean small floor areas not occupied by the people.
$floorBrush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(150,151,148))
$g.FillPolygon($floorBrush,[System.Drawing.Point[]]@(
    (New-Object System.Drawing.Point 230,708),(New-Object System.Drawing.Point 246,708),
    (New-Object System.Drawing.Point 246,750),(New-Object System.Drawing.Point 218,750)))
$floorBrush.Dispose()
$g.Dispose()

# Apply a restrained cool-neutral corporate grade to the complete photograph.
$graded = New-Object System.Drawing.Bitmap 1000,750
$gg = [System.Drawing.Graphics]::FromImage($graded)
$matrix = New-Object System.Drawing.Imaging.ColorMatrix
$matrix.Matrix00 = 1.03; $matrix.Matrix11 = 1.04; $matrix.Matrix22 = 1.08
$matrix.Matrix40 = -0.025; $matrix.Matrix41 = -0.020; $matrix.Matrix42 = -0.010
$attributes = New-Object System.Drawing.Imaging.ImageAttributes
$attributes.SetColorMatrix($matrix)
$attributes.SetGamma(0.94)
$gg.DrawImage($base,(New-Object System.Drawing.Rectangle 0,0,1000,750),0,0,1000,750,[System.Drawing.GraphicsUnit]::Pixel,$attributes)
$attributes.Dispose()
$gg.Dispose()
$base.Dispose()
$graded.Save($Output,[System.Drawing.Imaging.ImageFormat]::Png)
$graded.Dispose()
Write-Output $Output
