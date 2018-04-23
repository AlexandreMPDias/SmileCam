############## PYINSTALLER

set-location "pyinstaller"
.\run.bat

############### INNO SETUP

set-location "..\innosetup"
.\run.bat

############## DESKTOP APP CONVERTER

set-location "..\appx"
& .\run.ps1