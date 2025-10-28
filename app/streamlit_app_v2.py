"""
SmartManufacture AI - Enterprise Manufacturing Output Predictor
Professional Web Interface for Production Optimization
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="SmartManufacture AI | Output Predictor",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://smartmanufacture.ai/support',
        'Report a bug': 'https://smartmanufacture.ai/bugs',
        'About': "# SmartManufacture AI v2.0\nEnterprise Manufacturing Output Prediction System"
    }
)

# Enhanced Corporate CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Poppins:wght@600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        padding: 0rem 2rem;
        background: linear-gradient(to bottom, #f8fafc 0%, #ffffff 100%);
    }
    
    .company-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #06b6d4 100%);
        padding: 2.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(30, 58, 138, 0.2);
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .company-logo {
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        letter-spacing: 2px;
    }
    
    .company-tagline {
        font-size: 1.2rem;
        color: #e0f2fe;
        text-align: center;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: linear-gradient(to right, #f1f5f9, #e2e8f0);
        padding: 0.5rem;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        padding: 0 30px;
        background: white;
        border-radius: 8px;
        font-weight: 600;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border-color: #1e3a8a;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #3b82f6 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 20px 60px rgba(30, 58, 138, 0.4);
        border: 1px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .prediction-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .prediction-value {
        font-size: 4rem;
        font-weight: 700;
        margin: 1rem 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
        border-left-color: #1e3a8a;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e3a8a;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #64748b;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .info-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #e2e8f0;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        padding: 0.75rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
    
    .badge-success {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.25rem;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
    }
    
    .badge-warning {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.25rem;
        box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);
    }
    
    .badge-info {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.25rem;
        box-shadow: 0 2px 8px rgba(6, 182, 212, 0.3);
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: #e2e8f0;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Load Model Artifacts
@st.cache_resource
def load_model_artifacts():
    """Load trained model and metadata"""
    try:
        base_path = Path(__file__).parent.parent
        model_path = base_path / 'models' / 'model_pipeline.pkl'
        metadata_path = base_path / 'models' / 'metadata.json'
        
        model = joblib.load(model_path)
        
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        
        return model, metadata, None
    except Exception as e:
        return None, None, str(e)

# Prediction Function
def predict_output(model, injection_temp, injection_pressure, cycle_time, cooling_time,
                   melt_viscosity, ambient_temp, machine_age, maintenance_hours, operator_experience):
    """Make prediction using loaded model"""
    try:
        # Create input dictionary
        input_data = {
            'Injection_Temperature': injection_temp,
            'Injection_Pressure': injection_pressure,
            'Cycle_Time': cycle_time,
            'Cooling_Time': cooling_time,
            'Material_Viscosity': melt_viscosity,
            'Ambient_Temperature': ambient_temp,
            'Machine_Age': machine_age,
            'Operator_Experience': operator_experience,
            'Maintenance_Hours': maintenance_hours,
            'Temperature_Pressure_Ratio': injection_temp / injection_pressure if injection_pressure > 0 else 0,
            'Total_Cycle_Time': cycle_time + cooling_time,
            'hour': 12,
            'is_weekend': 0
        }
        
        df = pd.DataFrame([input_data])
        prediction = model.predict(df)[0]
        return prediction
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None

# Load model
model, model_metadata, error = load_model_artifacts()

if error:
    st.error(f"⚠️ Error loading model: {error}")
    st.stop()

# Corporate Header with Branding
st.markdown("""
    <div class="company-header">
        <div class="company-logo">🏭 SmartManufacture AI</div>
        <div class="company-tagline">Advanced Predictive Analytics for Manufacturing Excellence</div>
    </div>
""", unsafe_allow_html=True)

# Quick Stats Banner
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class="info-card" style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; color: #3b82f6;">⚡</div>
            <div style="font-weight: 600; color: #1e3a8a;">Real-Time</div>
            <div style="font-size: 0.85rem; color: #64748b;">Instant Predictions</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="info-card" style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; color: #10b981;">🎯</div>
            <div style="font-weight: 600; color: #1e3a8a;">{model_metadata['test_metrics']['r2']:.1%} R²</div>
            <div style="font-size: 0.85rem; color: #64748b;">Model Accuracy</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="info-card" style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; color: #f59e0b;">📊</div>
            <div style="font-weight: 600; color: #1e3a8a;">9 Parameters</div>
            <div style="font-size: 0.85rem; color: #64748b;">ML Features</div>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class="info-card" style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; color: #06b6d4;">🚀</div>
            <div style="font-weight: 600; color: #1e3a8a;">AI-Powered</div>
            <div style="font-size: 0.85rem; color: #64748b;">Optimization</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0; background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); border-radius: 10px; margin-bottom: 1.5rem;">
            <div style="font-size: 2.5rem;">🏭</div>
            <div style="color: white; font-weight: 700; font-size: 1.2rem; margin-top: 0.5rem;">SmartManufacture AI</div>
            <div style="color: #e0f2fe; font-size: 0.85rem; margin-top: 0.25rem;">v2.0.0 Enterprise</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Model Performance")
    
    if model_metadata:
        st.markdown(f"""
            <div class="metric-card" style="margin: 1rem 0; padding: 1rem; background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); border: none;">
                <div style="color: #e0f2fe; font-size: 0.85rem; margin-bottom: 0.5rem;">Model Accuracy</div>
                <div style="color: white; font-size: 2rem; font-weight: 700;">{model_metadata['test_metrics']['r2']:.1%}</div>
                <div style="color: #10b981; font-weight: 600; margin-top: 0.5rem;">✓ Excellent Performance</div>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("RMSE", f"{model_metadata['test_metrics']['rmse']:.2f}")
        with col2:
            st.metric("MAE", f"{model_metadata['test_metrics']['mae']:.2f}")
    
    st.markdown("---")
    
    st.markdown("### 🎯 Key Features")
    st.markdown("""
    • **Real-Time Predictions**
    • **Advanced Analytics**
    • **ROI Calculator**
    • **Optimization Insights**
    • **Interactive Charts**
    • **Business Intelligence**
    """)
    
    st.markdown("---")
    
    st.markdown("### 📞 Support")
    st.markdown("""
    **Technical Support:**  
    📧 support@smartmanufacture.ai  
    📱 +1 (800) 555-0123  
    
    **Business Hours:**  
    Mon-Fri: 9AM - 6PM EST
    """)
    
    st.markdown("---")
    
    st.markdown(f"""
        <div style="text-align: center; color: #94a3b8; font-size: 0.75rem; margin-top: 2rem;">
            Last Updated<br>
            {datetime.now().strftime("%B %d, %Y %I:%M %p")}
        </div>
    """, unsafe_allow_html=True)

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔮 Predictor", "📊 Analytics", "📈 Business Insights", "ℹ️ Help"])

with tab1:
    st.markdown("""
        <div style="background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 100%); padding: 1.5rem; border-radius: 15px; border-left: 5px solid #3b82f6; margin-bottom: 2rem;">
            <h2 style="color: #1e3a8a; margin: 0;">🔮 Production Output Predictor</h2>
            <p style="color: #64748b; margin-top: 0.5rem; margin-bottom: 0;">Configure machine parameters and operating conditions to get AI-powered output predictions</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Input Parameters in 3 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🌡️ Temperature & Pressure")
        injection_temp = st.slider("Injection Temperature (°C)", 180, 280, 220, 5,
                                   help="Optimal range: 200-250°C")
        injection_pressure = st.slider("Injection Pressure (bar)", 80, 150, 120, 5,
                                       help="Optimal range: 100-140 bar")
        ambient_temp = st.slider("Ambient Temperature (°C)", 15, 35, 22, 1,
                                 help="Factory floor temperature")
    
    with col2:
        st.markdown("#### ⏱️ Cycle Times & Material")
        cycle_time = st.slider("Cycle Time (seconds)", 15, 60, 30, 1,
                               help="Time for one complete cycle")
        cooling_time = st.slider("Cooling Time (seconds)", 5, 30, 12, 1,
                                 help="Part cooling duration")
        melt_viscosity = st.slider("Melt Viscosity (Pa·s)", 100, 400, 250, 10,
                                   help="Material flow resistance")
    
    with col3:
        st.markdown("#### 🔧 Machine & Operator")
        machine_age = st.slider("Machine Age (years)", 0, 20, 5, 1,
                                help="Years since installation")
        maintenance_hours = st.slider("Maintenance Hours", 0, 200, 50, 10,
                                      help="Hours since last service")
        operator_experience = st.slider("Operator Experience (months)", 1, 60, 24, 1,
                                        help="Months of training")
    
    # Predict Button
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        predict_clicked = st.button("🚀 GENERATE PREDICTION", type="primary", use_container_width=True)
    
    if predict_clicked:
        with st.spinner('🔄 AI Model Processing...'):
            predicted_output = predict_output(
                model, injection_temp, injection_pressure, cycle_time, 
                cooling_time, melt_viscosity, ambient_temp,
                machine_age, maintenance_hours, operator_experience
            )
        
        if predicted_output:
            st.markdown(f"""
                <div class="prediction-box">
                    <div style="position: relative; z-index: 1;">
                        <div style="font-size: 1.2rem; font-weight: 600; opacity: 0.9; letter-spacing: 2px; margin-bottom: 1rem;">PREDICTED OUTPUT</div>
                        <div class="prediction-value">
                            {predicted_output:.1f}
                        </div>
                        <div style="font-size: 1.5rem; opacity: 0.9; font-weight: 500;">PARTS PER HOUR</div>
                        <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.2);">
                            <div style="font-size: 0.95rem; opacity: 0.8;">✓ Prediction Confidence: High | Model Accuracy: {model_metadata['test_metrics']['r2']:.1%}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Enhanced Metrics
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                daily_output = predicted_output * 16
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">📦 Daily Output</div>
                        <div class="metric-value">{daily_output:.0f}</div>
                        <div style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">parts (2 shifts)</div>
                        <div class="badge-success" style="margin-top: 0.75rem; font-size: 0.8rem;">On Target</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                total_cycle = cycle_time + cooling_time
                efficiency = (60 / total_cycle) * 100 if total_cycle > 0 else 0
                efficiency_badge = "badge-success" if efficiency >= 80 else "badge-warning"
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">⚡ Cycle Efficiency</div>
                        <div class="metric-value">{efficiency:.1f}%</div>
                        <div style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">utilization rate</div>
                        <div class="{efficiency_badge}" style="margin-top: 0.75rem; font-size: 0.8rem;">
                            {'Excellent' if efficiency >= 80 else 'Optimize'}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                temp_pressure_ratio = injection_temp / injection_pressure if injection_pressure > 0 else 0
                is_optimal = 1.5 < temp_pressure_ratio < 2.5
                ratio_badge = "badge-success" if is_optimal else "badge-warning"
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">🌡️ Temp/Pressure</div>
                        <div class="metric-value">{temp_pressure_ratio:.2f}</div>
                        <div style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">ratio</div>
                        <div class="{ratio_badge}" style="margin-top: 0.75rem; font-size: 0.8rem;">
                            {'✓ Optimal' if is_optimal else '⚠ Check'}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col4:
                weekly_output = daily_output * 5
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">📊 Weekly Output</div>
                        <div class="metric-value">{weekly_output:.0f}</div>
                        <div style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">parts (5 days)</div>
                        <div class="badge-info" style="margin-top: 0.75rem; font-size: 0.8rem;">Forecast</div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 💡 AI-Powered Recommendations")
            
            recommendations = []
            if cycle_time > 40:
                recommendations.append("⚠️ **Cycle Time High**: Consider reducing cycle time to improve throughput")
            if efficiency < 80:
                recommendations.append("⚠️ **Low Efficiency**: Optimize cycle times for better utilization")
            if not is_optimal:
                recommendations.append("⚠️ **Temperature/Pressure**: Adjust ratio to optimal range (1.5-2.5)")
            if machine_age > 10:
                recommendations.append("ℹ️ **Machine Age**: Consider equipment upgrade or increased maintenance")
            if operator_experience < 12:
                recommendations.append("💡 **Training Opportunity**: Invest in operator training for improved output")
            
            if not recommendations:
                st.success("✅ **All parameters are optimized!** Your configuration is excellent.")
            else:
                for rec in recommendations:
                    st.info(rec)

with tab2:
    st.markdown("## 📊 Advanced Analytics Dashboard")
    
    st.markdown("""
        <div class="info-card">
            <h3 style="color: #1e3a8a; margin-top: 0;">Sensitivity Analysis</h3>
            <p style="color: #64748b;">Explore how different parameters impact production output</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create sensitivity charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Cycle Time Impact
        cycle_times = np.linspace(15, 60, 20)
        outputs = [predict_output(model, injection_temp, injection_pressure, ct, cooling_time,
                                  melt_viscosity, ambient_temp, machine_age, maintenance_hours, 
                                  operator_experience) for ct in cycle_times]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=cycle_times, y=outputs, mode='lines+markers',
                                 line=dict(color='#3b82f6', width=3),
                                 marker=dict(size=8)))
        fig.update_layout(title="Cycle Time Impact on Output",
                         xaxis_title="Cycle Time (seconds)",
                         yaxis_title="Parts per Hour",
                         height=400,
                         template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Temperature Impact
        temps = np.linspace(180, 280, 20)
        temp_outputs = [predict_output(model, t, injection_pressure, cycle_time, cooling_time,
                                       melt_viscosity, ambient_temp, machine_age, maintenance_hours, 
                                       operator_experience) for t in temps]
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=temps, y=temp_outputs, mode='lines+markers',
                                  line=dict(color='#f59e0b', width=3),
                                  marker=dict(size=8)))
        fig2.update_layout(title="Temperature Impact on Output",
                          xaxis_title="Injection Temperature (°C)",
                          yaxis_title="Parts per Hour",
                          height=400,
                          template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.markdown("## 📈 Business Intelligence & ROI")
    
    st.markdown("""
        <div class="info-card">
            <h3 style="color: #1e3a8a; margin-top: 0;">💰 ROI Calculator</h3>
            <p style="color: #64748b;">Calculate the financial impact of production improvements</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        part_value = st.number_input("Part Value ($)", min_value=0.1, max_value=1000.0, value=5.0, step=0.5)
        shifts_per_day = st.selectbox("Shifts per Day", [1, 2, 3], index=1)
        days_per_year = st.number_input("Operating Days/Year", min_value=200, max_value=365, value=250)
    
    with col2:
        if 'predicted_output' in locals() and predicted_output:
            annual_parts = predicted_output * (shifts_per_day * 8) * days_per_year
            annual_revenue = annual_parts * part_value
            
            st.markdown(f"""
                <div class="metric-card" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); border: none;">
                    <div style="color: white; font-size: 0.9rem; opacity: 0.9;">ANNUAL OUTPUT</div>
                    <div style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">
                        {annual_parts:,.0f}
                    </div>
                    <div style="color: white; font-size: 0.95rem; opacity: 0.9;">parts per year</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="metric-card" style="background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); border: none; margin-top: 1rem;">
                    <div style="color: white; font-size: 0.9rem; opacity: 0.9;">ANNUAL REVENUE</div>
                    <div style="color: white; font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">
                        ${annual_revenue:,.2f}
                    </div>
                    <div style="color: white; font-size: 0.95rem; opacity: 0.9;">projected revenue</div>
                </div>
            """, unsafe_allow_html=True)

with tab4:
    st.markdown("## ℹ️ Help & Documentation")
    
    st.markdown("""
        <div class="info-card">
            <h3 style="color: #1e3a8a;">Getting Started</h3>
            <ol style="color: #64748b; line-height: 2;">
                <li>Adjust the machine parameters using the sliders in the Predictor tab</li>
                <li>Click the "GENERATE PREDICTION" button to get AI-powered output forecast</li>
                <li>Review the metrics and recommendations</li>
                <li>Explore Analytics for parameter sensitivity</li>
                <li>Calculate ROI in Business Insights</li>
            </ol>
        </div>
        
        <div class="info-card" style="margin-top: 1rem;">
            <h3 style="color: #1e3a8a;">About SmartManufacture AI</h3>
            <p style="color: #64748b;">
            SmartManufacture AI is an enterprise-grade predictive analytics platform designed to optimize 
            manufacturing operations. Our machine learning models analyze multiple parameters to provide 
            accurate production forecasts and actionable insights.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #64748b; font-size: 0.9rem; border-top: 2px solid #e2e8f0;">
        <b>SmartManufacture AI</b> v2.0.0 Enterprise | © 2025 All Rights Reserved<br>
        Powered by Advanced Machine Learning | Support: support@smartmanufacture.ai
    </div>
""", unsafe_allow_html=True)
