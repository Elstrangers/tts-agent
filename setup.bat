@echo off
REM TTS Agent Setup Script for Windows
REM Quick setup and test

echo.
echo ========================================
echo TTS Agent - Windows Setup
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo [1/4] Python found. Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [2/4] Dependencies installed.
echo.

REM Check for .env file
if not exist .env (
    echo [3/4] Creating .env file from template...
    copy .env.example .env
    echo Please edit .env and set your GEMINI_API_KEY
    echo.
    pause
) else (
    echo [3/4] .env file already exists
)

echo [4/4] Running local tests...
python test_local.py

echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env and set GEMINI_API_KEY (if not already set)
echo 2. Run: python tts_generator.py "Your text here"
echo 3. Or push to GitHub and use GitHub Actions workflow
echo.
pause
