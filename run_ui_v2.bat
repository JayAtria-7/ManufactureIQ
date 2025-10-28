@echo off
echo ========================================
echo   SmartManufacture AI v2.0 Enterprise
echo   Manufacturing Output Predictor
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then install requirements: venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Checking dependencies...
python -c "import streamlit, plotly, pandas, numpy, sklearn, joblib" 2>nul
if errorlevel 1 (
    echo.
    echo Installing missing packages...
    pip install streamlit plotly pandas numpy scikit-learn joblib
)

echo.
echo ========================================
echo   Launching SmartManufacture AI v2.0
echo ========================================
echo.
echo The enhanced UI will open in your browser...
echo.
echo Features:
echo  - Professional corporate design
echo  - Animated prediction displays
echo  - Advanced analytics dashboard
echo  - ROI calculator
echo  - Interactive charts
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Launch the enhanced v2 UI
streamlit run app\streamlit_app_v2.py --server.port 8501

pause
