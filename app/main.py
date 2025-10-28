import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'model_pipeline.pkl')
METADATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'metadata.json')

app = FastAPI(title="Manufacturing Output Predictor", version="1.0")

# Load model lazily
_model = None
_metadata = None

class InputData(BaseModel):
    Injection_Temperature: float
    Injection_Pressure: float
    Cycle_Time: float
    Cooling_Time: float
    Material_Viscosity: float
    Ambient_Temperature: float
    Machine_Age: float
    Operator_Experience: float
    Maintenance_Hours: float

@app.on_event("startup")
def load_artifacts():
    global _model, _metadata
    try:
        _model = joblib.load(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
    except Exception as e:
        print(f"Error loading model: {e}")
        _model = None
    
    try:
        import json
        with open(METADATA_PATH, 'r') as f:
            _metadata = json.load(f)
        print(f"Metadata loaded from {METADATA_PATH}")
    except Exception as e:
        print(f"Error loading metadata: {e}")
        _metadata = None

@app.get("/")
def root():
    return {"message": "Manufacturing Output Predictor API", "status": "running"}

@app.get("/health")
def health():
    return {
        "status": "ok", 
        "model_loaded": _model is not None,
        "metadata_loaded": _metadata is not None
    }

@app.get("/metadata")
def get_metadata():
    if _metadata is None:
        raise HTTPException(status_code=503, detail="Metadata not loaded")
    return _metadata

@app.post("/predict")
def predict(payload: InputData):
    if _model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # Create derived features (must match training)
    temp_pressure_ratio = payload.Injection_Temperature / payload.Injection_Pressure
    total_cycle_time = payload.Cycle_Time + payload.Cooling_Time
    
    # Construct feature DataFrame (must match training feature order)
    # Based on metadata: ['Injection_Temperature', 'Injection_Pressure', 'Cycle_Time', 
    # 'Cooling_Time', 'Material_Viscosity', 'Ambient_Temperature', 'Machine_Age', 
    # 'Operator_Experience', 'Maintenance_Hours', 'Temperature_Pressure_Ratio', 
    # 'Total_Cycle_Time', 'hour', 'is_weekend']
    
    # For API we'll use default values for time-based features
    hour = 12  # midday default
    is_weekend = 0  # weekday default
    
    x = pd.DataFrame([{
        'Injection_Temperature': payload.Injection_Temperature,
        'Injection_Pressure': payload.Injection_Pressure,
        'Cycle_Time': payload.Cycle_Time,
        'Cooling_Time': payload.Cooling_Time,
        'Material_Viscosity': payload.Material_Viscosity,
        'Ambient_Temperature': payload.Ambient_Temperature,
        'Machine_Age': payload.Machine_Age,
        'Operator_Experience': payload.Operator_Experience,
        'Maintenance_Hours': payload.Maintenance_Hours,
        'Temperature_Pressure_Ratio': temp_pressure_ratio,
        'Total_Cycle_Time': total_cycle_time,
        'hour': hour,
        'is_weekend': is_weekend
    }])
    
    try:
        pred = _model.predict(x)
        return {
            "predicted_parts_per_hour": float(pred[0]),
            "input": payload.dict(),
            "derived_features": {
                "Temperature_Pressure_Ratio": temp_pressure_ratio,
                "Total_Cycle_Time": total_cycle_time
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
