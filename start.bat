@echo off
echo ========================================
echo Daily GitHub Commits - Starting...
echo ========================================
echo.

REM Check if requirements are installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Installing requirements...
    pip install -r requirements.txt
    echo.
)

echo Starting automatic commit system...
echo.
echo The system will:
echo   - Make 7-10 commits daily automatically
echo   - Push all commits to GitHub
echo   - Run in the background
echo.
echo Web UI: http://localhost:5000
echo.
echo Press Ctrl+C to stop
echo.

python app.py
pause

