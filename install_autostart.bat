@echo off
echo ========================================
echo GitHub Daily Commits - Auto-Start Setup
echo ========================================
echo.
echo This will add the application to Windows Startup
echo so it runs automatically when you log in.
echo.

set SCRIPT_DIR=%~dp0
set STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SHORTCUT_NAME=GitHub Daily Commits.lnk

echo Creating startup shortcut...
echo.

REM Create VBScript to create shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%TEMP%\create_shortcut.vbs"
echo sLinkFile = "%STARTUP_DIR%\%SHORTCUT_NAME%" >> "%TEMP%\create_shortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%TEMP%\create_shortcut.vbs"
echo oLink.TargetPath = "pythonw.exe" >> "%TEMP%\create_shortcut.vbs"
echo oLink.Arguments = """%SCRIPT_DIR%app.py""" >> "%TEMP%\create_shortcut.vbs"
echo oLink.WorkingDirectory = "%SCRIPT_DIR%" >> "%TEMP%\create_shortcut.vbs"
echo oLink.WindowStyle = 1 >> "%TEMP%\create_shortcut.vbs"
echo oLink.Save >> "%TEMP%\create_shortcut.vbs"

cscript //nologo "%TEMP%\create_shortcut.vbs"
del "%TEMP%\create_shortcut.vbs"

if exist "%STARTUP_DIR%\%SHORTCUT_NAME%" (
    echo.
    echo ✓ Successfully added to Windows Startup!
    echo.
    echo The application will now start automatically when you log in.
    echo You can remove it from Startup folder if needed.
) else (
    echo.
    echo ✗ Failed to create startup shortcut.
    echo Please run this script as Administrator.
)

echo.
pause

