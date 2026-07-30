param(
    [ValidateSet('include', 'exclude')]
    [string]$EnterpriseKnowledgeDecision,
    [switch]$UserConfirmedThisRun
)

if (-not $EnterpriseKnowledgeDecision) {
    Write-Error 'PACKAGING_GATE: Ask the user whether to include 企业知识（保密） in this package.'
    exit 2
}
if ($EnterpriseKnowledgeDecision -eq 'include' -and -not $UserConfirmedThisRun) {
    Write-Error 'PACKAGING_GATE: Inclusion requires an explicit yes from the user for this packaging run.'
    exit 3
}

Write-Output "PASS: enterprise knowledge packaging decision = $EnterpriseKnowledgeDecision"
