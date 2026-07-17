param(
    [string]$Background = "C:\Users\Lostk\Documents\B2B机加工生图\output\people-preserved-composite\background-crop.png",
    [string]$PeopleSource = "C:\Users\Lostk\Documents\B2B机加工生图\input\factory-retouch\06-people-locked-target.png",
    [string]$Output = "C:\Users\Lostk\Documents\B2B机加工生图\output\people-preserved-composite\factory-people-preserved-final.png"
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$scale = 4
function New-ScaledPath([array]$Coordinates) {
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $points = New-Object 'System.Collections.Generic.List[System.Drawing.PointF]'
    foreach ($pair in $Coordinates) {
        $points.Add((New-Object System.Drawing.PointF ([single]($pair[0]*$scale)),([single]($pair[1]*$scale))))
    }
    $path.AddPolygon($points.ToArray())
    return $path
}

$leftHead = @(
    @(88,250),@(115,244),@(139,248),@(157,260),@(170,280),@(178,302),@(179,327),@(193,341),
    @(201,357),@(196,372),@(201,383),@(191,398),@(178,405),@(163,399),@(150,391),@(137,383),
    @(128,371),@(115,357),@(104,339),@(91,323),@(80,304),@(76,282),@(79,263)
)

$leftBody = @(
    @(132,370),@(151,387),@(180,399),@(205,411),@(219,430),@(227,461),@(228,493),@(224,529),
    @(230,573),@(229,611),@(224,652),@(215,683),@(198,705),@(189,728),@(187,750),@(0,750),
    @(0,365),@(27,350),@(52,334),@(76,330),@(98,344),@(116,356)
)

$rightHead = @(
    @(583,200),@(612,194),@(640,199),@(663,210),@(684,230),@(697,257),@(699,283),@(690,305),
    @(677,318),@(657,326),@(634,325),@(612,317),@(590,307),@(571,294),@(558,276),@(553,252),
    @(558,226),@(568,208)
)

$rightBody = @(
    @(548,282),@(570,300),@(594,313),@(622,320),@(651,321),@(680,311),@(709,316),@(734,330),
    @(757,349),@(776,374),@(789,406),@(799,443),@(806,484),@(805,524),@(798,564),@(786,600),
    @(770,626),@(750,646),@(739,654),@(735,689),@(727,750),@(520,750),@(516,707),@(498,680),
    @(478,649),@(463,616),@(455,580),@(451,545),@(440,507),@(437,474),@(442,439),@(446,401),
    @(449,371),@(459,348),@(478,332),@(505,319),@(529,306)
)

$leftHeadPath = New-ScaledPath $leftHead
$leftBodyPath = New-ScaledPath $leftBody
$rightHeadPath = New-ScaledPath $rightHead
$rightBodyPath = New-ScaledPath $rightBody
$backgroundImage = [System.Drawing.Image]::FromFile($Background)
$peopleImage = [System.Drawing.Image]::FromFile($PeopleSource)
$largeCanvas = New-Object System.Drawing.Bitmap 4000,3000
$largeGraphics = [System.Drawing.Graphics]::FromImage($largeCanvas)
$largeGraphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
$largeGraphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$largeGraphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$largeGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$largeGraphics.DrawImage($backgroundImage,0,0,4000,3000)

$peopleRegion = New-Object System.Drawing.Region $leftHeadPath
$peopleRegion.Union($leftBodyPath)
$peopleRegion.Union($rightHeadPath)
$peopleRegion.Union($rightBodyPath)
$largeGraphics.SetClip($peopleRegion,[System.Drawing.Drawing2D.CombineMode]::Replace)
$largeGraphics.DrawImage($peopleImage,0,0,4000,3000)
$largeGraphics.ResetClip()

$largeGraphics.Dispose()
$backgroundImage.Dispose()
$peopleImage.Dispose()
$peopleRegion.Dispose()
$leftHeadPath.Dispose()
$leftBodyPath.Dispose()
$rightHeadPath.Dispose()
$rightBodyPath.Dispose()

$canvas = New-Object System.Drawing.Bitmap 1000,750
$graphics = [System.Drawing.Graphics]::FromImage($canvas)
$graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.DrawImage($largeCanvas,0,0,1000,750)
$graphics.Dispose()
$largeCanvas.Dispose()
$canvas.Save($Output,[System.Drawing.Imaging.ImageFormat]::Png)
$canvas.Dispose()
Write-Output $Output
