@echo off
if exist pyinstaller_log.txt (
    del pyinstaller_log.txt
)
if exist dist (
    rmdir /s /q dist 1> NUL 2>&1
)
if exist build (
    rmdir /s /q build 1> NUL 2>&1
)
echo [ Pyinstaller ]: Starting
pyinstaller main.spec 
:1>> pyinstaller_log.txt 2>>&1
echo [ Pyinstaller ]: Done
echo Log copied to: [ pyinstaller_log.txt ]
