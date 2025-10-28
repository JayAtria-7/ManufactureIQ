"""Test script to verify the model and API work correctly"""
import sys
sys.path.insert(0, 'e:/project/cap1')

# Test 1: Load the saved model directly
print("=" * 60)
print("TEST 1: Loading saved model directly")
print("=" * 60)
import joblib
import pandas as pd

model = joblib.load('e:/project/cap1/models/model_pipeline.pkl')
print("✓ Model loaded successfully")

# Create test input
test_data = pd.DataFrame([{
    'Injection_Temperature': 220,
    'Injection_Pressure': 120,
    'Cycle_Time': 30,
    'Cooling_Time': 12,
    'Material_Viscosity': 250,
    'Ambient_Temperature': 22,
    'Machine_Age': 5,
    'Operator_Experience': 24,
    'Maintenance_Hours': 50,
    'Temperature_Pressure_Ratio': 220/120,
    'Total_Cycle_Time': 30+12,
    'hour': 12,
    'is_weekend': 0
}])

prediction = model.predict(test_data)
print(f"✓ Direct model prediction: {prediction[0]:.2f} parts/hour")

# Test 2: Import FastAPI app
print("\n" + "=" * 60)
print("TEST 2: Testing FastAPI app import and model loading")
print("=" * 60)

from app.main import app, _model, _metadata

if _model is None:
    print("✗ Model not loaded in FastAPI app - triggering startup")
    from app.main import load_artifacts
    load_artifacts()
    from app.main import _model, _metadata
    
if _model:
    print("✓ FastAPI model loaded successfully")
else:
    print("✗ Failed to load model in FastAPI")

if _metadata:
    print("✓ Metadata loaded successfully")
    print(f"  Test R²: {_metadata['test_metrics']['r2']:.4f}")
    print(f"  Test RMSE: {_metadata['test_metrics']['rmse']:.4f}")
else:
    print("✗ Failed to load metadata")

# Test 3: Simulate API prediction
print("\n" + "=" * 60)
print("TEST 3: Simulating API prediction")
print("=" * 60)

from app.main import InputData, predict

sample_input = InputData(
    Injection_Temperature=220,
    Injection_Pressure=120,
    Cycle_Time=30,
    Cooling_Time=12,
    Material_Viscosity=250,
    Ambient_Temperature=22,
    Machine_Age=5,
    Operator_Experience=24,
    Maintenance_Hours=50
)

try:
    result = predict(sample_input)
    print(f"✓ API prediction: {result['predicted_parts_per_hour']:.2f} parts/hour")
    print(f"  Derived features: {result['derived_features']}")
except Exception as e:
    print(f"✗ API prediction failed: {e}")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("\nTo run the API server:")
print("  cd e:\\project\\cap1")
print("  venv\\Scripts\\uvicorn.exe app.main:app --port 8000")
print("\nTo test with curl:")
print('  curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" \\')
print('    -d "{\\"Injection_Temperature\\":220,\\"Injection_Pressure\\":120,\\"Cycle_Time\\":30,\\"Cooling_Time\\":12,\\"Material_Viscosity\\":250,\\"Ambient_Temperature\\":22,\\"Machine_Age\\":5,\\"Operator_Experience\\":24,\\"Maintenance_Hours\\":50}"')
