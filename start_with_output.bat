@echo off
cd /d "%~dp0"
echo ========================================
echo Starting Daily GitHub Commits...
echo ========================================
echo.
python app.py
pause

