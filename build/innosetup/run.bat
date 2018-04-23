@echo off
if EXIST Output (
    rmdir /s /q Output\\*
)
iscc /Qp InnoSetup.iss
:rmdir /s /q ..\\pyinstaller\\build ..\\pyinstaller\\dist