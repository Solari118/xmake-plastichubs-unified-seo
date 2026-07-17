param(
    [string]$SourcePath = "C:\Users\Lostk\Documents\B2B机加工生图\input\factory-retouch\06-people-locked-target.png",
    [string]$Output = "C:\Users\Lostk\Documents\B2B机加工生图\output\people-preserved-composite\factory-people-preserved-selective-clean.png"
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$source = [System.Drawing.Image]::FromFile($SourcePath)
$small = New-Object System.Drawing.Bitmap 125,94
$sg = [System.Drawing.Graphics]::FromImage($small)
$sg.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBilinear
$sg.DrawImage($source,0,0,125,94)
$sg.Dispose()

$large = New-Object System.Drawing.Bitmap 4000,3000
$lg = [System.Drawing.Graphics]::FromImage($large)
$lg.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$lg.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$lg.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$lg.DrawImage($small,0,0,4000,3000)
$small.Dispose()

function New-Path([array]$Coordinates) {
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $points = New-Object 'System.Collections.Generic.List[System.Drawing.PointF]'
    foreach ($pair in $Coordinates) {
        $points.Add((New-Object System.Drawing.PointF ([single]($pair[0]*4)),([single]($pair[1]*4))))
    }
    $path.AddPolygon($points.ToArray())
    return $path
}

$leftHead = @(@(88,250),@(115,244),@(139,248),@(157,260),@(170,280),@(178,302),@(179,327),@(193,341),@(201,357),@(196,372),@(201,383),@(191,398),@(178,405),@(163,399),@(150,391),@(137,383),@(128,371),@(115,357),@(104,339),@(91,323),@(80,304),@(76,282),@(79,263))
$leftBody = @(@(132,370),@(151,387),@(180,399),@(205,411),@(219,430),@(227,461),@(228,493),@(224,529),@(230,573),@(229,611),@(224,652),@(215,683),@(198,705),@(189,728),@(187,750),@(0,750),@(0,365),@(27,350),@(52,334),@(76,330),@(98,344),@(116,356))
$rightHead = @(@(583,200),@(612,194),@(640,199),@(663,210),@(684,230),@(697,257),@(699,283),@(690,305),@(677,318),@(657,326),@(634,325),@(612,317),@(590,307),@(571,294),@(558,276),@(553,252),@(558,226),@(568,208))
$rightBody = @(@(548,282),@(570,300),@(594,313),@(622,320),@(651,321),@(680,311),@(709,316),@(734,330),@(757,349),@(776,374),@(789,406),@(799,443),@(806,484),@(805,524),@(798,564),@(786,600),@(770,626),@(750,646),@(739,654),@(735,689),@(727,750),@(520,750),@(516,707),@(498,680),@(478,649),@(463,616),@(455,580),@(451,545),@(440,507),@(437,474),@(442,439),@(446,401),@(449,371),@(459,348),@(478,332),@(505,319),@(529,306))

$region = New-Object System.Drawing.Region (New-Object System.Drawing.Rectangle 2080,0,1920,2440)
$paths = @((New-Path $leftHead),(New-Path $leftBody),(New-Path $rightHead),(New-Path $rightBody))
foreach($path in $paths){$region.Union($path)}
$lg.SetClip($region,[System.Drawing.Drawing2D.CombineMode]::Replace)
$lg.DrawImage($source,0,0,4000,3000)
$lg.ResetClip()
$region.Dispose()
foreach($path in $paths){$path.Dispose()}
$source.Dispose()
$lg.Dispose()

$canvas = New-Object System.Drawing.Bitmap 1000,750
$g = [System.Drawing.Graphics]::FromImage($canvas)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.DrawImage($large,0,0,1000,750)
$large.Dispose()
$g.Dispose()

$graded = New-Object System.Drawing.Bitmap 1000,750
$gg = [System.Drawing.Graphics]::FromImage($graded)
$matrix = New-Object System.Drawing.Imaging.ColorMatrix
$matrix.Matrix00 = 1.02; $matrix.Matrix11 = 1.035; $matrix.Matrix22 = 1.075
$matrix.Matrix40 = -0.018; $matrix.Matrix41 = -0.014; $matrix.Matrix42 = -0.005
$attributes = New-Object System.Drawing.Imaging.ImageAttributes
$attributes.SetColorMatrix($matrix)
$attributes.SetGamma(0.95)
$gg.DrawImage($canvas,(New-Object System.Drawing.Rectangle 0,0,1000,750),0,0,1000,750,[System.Drawing.GraphicsUnit]::Pixel,$attributes)
$attributes.Dispose(); $gg.Dispose(); $canvas.Dispose()
$graded.Save($Output,[System.Drawing.Imaging.ImageFormat]::Png)
$graded.Dispose()
Write-Output $Output
