

$tenantID = "29ae2793-ba69-4a18-9c4e-70ec7fa86650"
$clientID = "985872de-7585-4c9d-b527-9695f1f19bea"
$clientsecret = "ONG8Q~5pM_JbjL5ko9m7fO~SdhwuF.KukA53UakQ"

$secureclientsecret = convertto-securestring $clientsecret -asplaintext -force

$credential = new-object system.management.automation.pscredential($clientid, $secureclientsecret)

connect-mggraph -tenantid $tenantid -clientsecretcredential $credential -nowelcome

[datetime]$date = (get-date).adddays(-7)
$sp = get-mgserviceprincipal -filter "createddatetime ge $date"
# $sp = get-mgserviceprincipal -filter "displayname eq 'check00'"
$sp

# $sp | %{ $_.displayname}
disconnect-mggraph

