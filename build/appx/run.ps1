$AppDisplayName = "SmileCam"
$PackageDisplayName = "Smile Cam - Holding your Smiles"
$PublisherName = "CN=Cyberlabs Ltda"
$CN = "Cyberlabs Ltda"

$LocalProjectPath = "C:\Users\tijuk\Projects\smile\build"
$destination = "$LocalProjectPath\appx\package"
$installer = "$LocalProjectPath\innosetup\Output\$AppDisplayName Setup.exe"


#Don't edit those:
$AppPath = "$destination\$AppDisplayName" 
$LocalVFSPath = "$AppPath\$AppDisplayName\VFS"
$ApplicationName = "$AppDisplayName.appx"
$cert = "auto-generated"

#Make Sure those are correct
$AppCertKit = "C:\Program Files (x86)\Windows Kits\10\App Certification Kit\"
$WindowsKitBinaries = "C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86"

function Copy_data {
    Copy-Item "$LocalVFSPath\$AppDisplayName\data" "$LocalVFSPath\SystemX64\data" -recurse
}

#####################################################################################
########################### DONT EDIT ANYTHING BELOW HERE ###########################
#####################################################################################



if (-not (Test-Path($destination))){
    New-Item -ItemType Directory -Force -Path $destination
}else{
    Remove-Item "package\*" -recurse
}


desktopappconverter.exe -installer $installer -installerArguments "/VERYSILENT /SUPPRESSMSGBOXES /NORESTART" `
                        -destination $destination -packagename $AppDisplayName -publisher $PublisherName -Version 0.0.0.1 `
                        -AppDisplayName $AppDisplayName `
                        -PackageDisplayName $PackageDisplayName `
                        -PackagePublisherDisplayName $AppDisplayName -makeappx -sign -verbose

Write-Host "Appx built"

Rename-Item "$AppPath\$AppDisplayName.appx" "$AppPath\$AppDisplayName.zip"
Expand-Archive "$AppPath\$AppDisplayName.zip" -DestinationPath "$AppPath\$AppDisplayName"
Remove-Item "$AppPath\$AppDisplayName.zip"
Copy_data

#set-location $AppCertKit
Write-Host "Making Appx"
& "$AppCertKit\makeappx.exe" pack /d "$AppPath\$AppDisplayName" /p "$AppPath\$ApplicationName"  /l  
Write-Host "Appx created"

Remove-Item "$AppPath\$AppDisplayName" -Recurse

if( Test-Path("$AppPath\$cert.cer")){
    Remove-Item "$AppPath\$cert.cer"
    Remove-Item "$AppPath\$cert.pfx"
}
#set-location $WindowsKitBinaries
if (-not (Test-Path("$AppPath\$cert.cer"))) {
    Write-Host "Certificates not found."
    makecert.exe -r -h 0 -n "CN=$CN" -eku 1.3.6.1.5.5.7.3.3 -pe -sv $AppPath\$cert.pvk $AppPath\$cert.cer
    pvk2pfx.exe -pvk $AppPath\$cert.pvk -spc $AppPath\$cert.cer -pfx $AppPath\$cert.pfx
    certutil.exe -addStore TrustedPeople $AppPath\$cert.cer
}
& "$WindowsKitBinaries\signtool.exe" sign -f $AppPath\$cert.pfx -fd SHA256 -v (Join-Path $AppPath  $ApplicationName)
& .\test.ps1
