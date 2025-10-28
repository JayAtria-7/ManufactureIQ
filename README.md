# 🏭 SmartManufacture AI - Manufacturing Output Predictor

## 🎨 **NEW v2.0: Enhanced Enterprise UI + FREE Cloud Deployment!**

### � What's New in v2.0:
- ✅ **Professional Corporate Design** - SmartManufacture AI branding with gradient themes
- ✅ **Animated UI Elements** - Pulsing predictions, smooth transitions, hover effects
- ✅ **Enhanced Color Palette** - Blue corporate gradient (#1e3a8a → #3b82f6 → #06b6d4)
- ✅ **Quick Stats Banner** - Real-time, Accuracy (85.9%), Parameters (9), AI-Powered
- ✅ **Advanced Sidebar** - Company logo, performance metrics, support contact
- ✅ **Better Typography** - Custom Google Fonts (Poppins + Inter)
- ✅ **4 Enhanced Metrics** - Daily/Weekly output, Cycle efficiency, Temp/Pressure ratio
- ✅ **Professional Footer** - Copyright, version info, support email
- ✅ **Cloud-Ready** - Deploy FREE to Streamlit Cloud (no credit card needed!)

### � Quick Start Options:

**Option 1: Enhanced UI v2.0 (Recommended)**
```cmd
run_ui_v2.bat
```
Or manually: `streamlit run app\streamlit_app_v2.py`

**Option 2: Original UI v1.0**
```cmd
run_ui.bat
```
Or manually: `streamlit run app\streamlit_app.py`

**Local Access:** http://localhost:8501

### 🌐 Deploy FREE Online (Streamlit Cloud):

Complete guide: **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**

**Quick Steps:**
1. Create public GitHub repository
2. Upload: `app/streamlit_app_v2.py`, `models/`, `.streamlit/config.toml`, `requirements_streamlit.txt`
3. Visit [share.streamlit.io](https://share.streamlit.io)
4. Connect GitHub → Select repo → Deploy!
5. Share your public URL with anyone! 🌍

**Cost:** $0/month forever (for public apps)

---

This project builds a linear regression model to predict parts produced per hour from machine operating parameters.

## Results Summary

✅ **Model Performance (Test Set)**
- **R² = 0.859** (Target: >0.75) ✓
- **RMSE = 4.30 parts/hour**
- **MAE = 3.40 parts/hour**

The model successfully exceeds the success criteria of R² > 0.75.

## Key Findings

**Top Predictive Features** (by absolute coefficient magnitude):
1. **Cycle_Time** (-5.35): Longer cycle time dramatically reduces output (expected)
2. **Total_Cycle_Time** (-4.85): Combined cycle+cooling time strongly impacts production
3. **Operator_Experience** (+3.81): More experienced operators produce significantly more parts
4. **Injection_Temperature** (+2.53): Higher temperature moderately increases output
5. **Machine_Age** (-1.82): Older machines produce fewer parts

**Manufacturing Recommendations**:
- **Reduce Cycle Time**: Every 1-second reduction in cycle time yields ~5.3 more parts/hour
- **Operator Training**: Invest in operator training (effect: +3.8 parts/hour per unit improvement)
- **Temperature Optimization**: Maintain injection temperature in optimal range (220-230°C)
- **Maintenance**: Schedule preventive maintenance to counteract machine age effects

## Files Created

- `capstone_manufacturing_lr.ipynb` - Full notebook with EDA, model training, evaluation, and model saving
- `requirements.txt` - Python dependencies
- `app/main.py` - FastAPI app to serve model predictions
- `Dockerfile` - Containerization for deployment
- `.dockerignore` - Docker ignore file
- `models/model_pipeline.pkl` - Trained model with preprocessing
- `models/preprocessor.pkl` - Standalone preprocessor
- `models/metadata.json` - Model metrics and feature list

## How to Run (Local)

### Option 1: Web UI (Recommended)

1. Create a virtual environment and install requirements:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Launch the Streamlit web interface:

```cmd
streamlit run app\streamlit_app.py
```

3. Your browser will automatically open to `http://localhost:8501`

**Features:**
- 🎨 Beautiful, interactive interface
- 📊 Real-time sensitivity analysis
- 💡 Automated recommendations
- 📈 Parameter impact visualization
- 💰 ROI calculator

### Option 2: Jupyter Notebook

1. Install requirements (if not done):

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Open and run `capstone_manufacturing_lr.ipynb` with Jupyter or VS Code.

### Option 3: FastAPI REST API

1. To run the API after model is saved:

```cmd
cd app
uvicorn main:app --reload --port 8000
```

4. Test the API:

```cmd
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"Injection_Temperature\":220,\"Injection_Pressure\":120,\"Cycle_Time\":30,\"Cooling_Time\":12,\"Material_Viscosity\":250,\"Ambient_Temperature\":22,\"Machine_Age\":5,\"Operator_Experience\":24,\"Maintenance_Hours\":50}"
```

## Docker Deployment (Optional)

Build and run the container:

```cmd
docker build -t manufacturing-predictor:latest .
docker run -p 8000:8000 manufacturing-predictor:latest
```

## Assumptions and Limitations

- **Dataset**: Uses provided 1,000-sample CSV (smaller than recommended 5,000+ samples)
- **Linear Model**: Assumes linear relationships; may not capture complex interactions
- **Feature Engineering**: Basic derived features; advanced interactions could improve performance
- **Temporal Effects**: Random train/test split used; production deployment should use time-based validation

## Next Steps for Improvement

If further optimization is needed:
- Collect more historical data (expand to 5,000+ samples)
- Try regularized regression (Ridge/Lasso) to reduce multicollinearity
- Add polynomial and interaction features
- Experiment with ensemble models (Random Forest, XGBoost)
- Implement time-series aware cross-validation
- Add confidence intervals for predictions
