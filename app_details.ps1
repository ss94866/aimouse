

$tenantID = "29ae2793-ba69-4a18-9c4e-70ec7fa86650"
$clientID = "985872de-7585-4c9d-b527-9695f1f19bea"
$clientsecret = "ONG8Q~5pM_JbjL5ko9m7fO~SdhwuF.KukA53UakQ"

$body = @{
  client_id = $clientid
  client_secret = $clientsecret
  scope = "https://graph.microsoft.com/.default"
  grant_type = "client_credentials"
}

$tokenresponse = invoke-restmethod -method Post -Uri "https://login.microsoftonline.com/$tenantID/oauth2/v2.0/token" -contenttype "application/x-www-form-urlencoded" -Body $body

$accesstoken = $tokenresponse.access_token

connect-mggraph -accesstoken $accesstoken

get-mgapplication -filter "displayname eq 'testauto'"

