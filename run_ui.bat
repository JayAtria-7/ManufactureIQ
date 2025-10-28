@echo off
REM Manufacturing Output Predictor - Easy Launcher
echo.
echo ========================================
echo   Manufacturing Output Predictor UI
echo ========================================
echo.

REM Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then: venv\Scripts\activate
    echo Then: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if streamlit is installed
echo [2/3] Checking dependencies...
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo [WARNING] Streamlit not found. Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies!
        pause
        exit /b 1
    )
)

REM Launch Streamlit
echo [3/3] Launching web interface...
echo.
echo ========================================
echo   Opening browser to http://localhost:8501
echo   Press Ctrl+C to stop the server
echo ========================================
echo.

streamlit run app\streamlit_app.py --server.port 8501 --server.headless false

pause
