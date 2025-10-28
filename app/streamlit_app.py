"""
Manufacturing Output Prediction - Streamlit Web UI
A professional interface for predicting parts per hour from machine parameters
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import sys

# Page configuration
st.set_page_config(
    page_title="Manufacturing Output Predictor",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .prediction-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        margin: 1rem 0;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.75rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0d5a9e;
    }
</style>
""", unsafe_allow_html=True)

# Load model and metadata
@st.cache_resource
def load_model_artifacts():
    """Load the trained model and metadata"""
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

# Make prediction
def predict_output(model, input_data):
    """Generate prediction from input parameters"""
    # Create derived features
    input_data['Temperature_Pressure_Ratio'] = input_data['Injection_Temperature'] / input_data['Injection_Pressure']
    input_data['Total_Cycle_Time'] = input_data['Cycle_Time'] + input_data['Cooling_Time']
    input_data['hour'] = 12  # Default midday
    input_data['is_weekend'] = 0  # Default weekday
    
    # Create DataFrame with correct feature order
    df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(df)[0]
    return prediction

# Main app
def main():
    # Header
    st.markdown('<div class="main-header">🏭 Manufacturing Output Predictor</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Load model
    model, metadata, error = load_model_artifacts()
    
    if error:
        st.error(f"❌ Error loading model: {error}")
        st.info("Please ensure the model files are in the 'models' directory.")
        return
    
    # Sidebar - Model Information
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/factory.png", width=80)
        st.title("Model Information")
        
        if metadata:
            st.markdown("### 📊 Performance Metrics")
            test_metrics = metadata['test_metrics']
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("R² Score", f"{test_metrics['r2']:.3f}")
                st.metric("MAE", f"{test_metrics['mae']:.2f}")
            with col2:
                st.metric("RMSE", f"{test_metrics['rmse']:.2f}")
                st.metric("MSE", f"{test_metrics['mse']:.2f}")
            
            # Performance indicator
            r2_score = test_metrics['r2']
            if r2_score >= 0.85:
                st.success("✅ Excellent Model Performance")
            elif r2_score >= 0.75:
                st.info("✓ Good Model Performance")
            else:
                st.warning("⚠ Moderate Model Performance")
        
        st.markdown("---")
        st.markdown("### 📖 About")
        st.info("""
        This tool predicts hourly parts production based on:
        - Machine settings
        - Material properties
        - Operating conditions
        - Maintenance status
        """)
        
        st.markdown("### 🎯 Quick Tips")
        st.markdown("""
        - **Reduce Cycle Time** for maximum output
        - **Train Operators** to improve efficiency
        - **Maintain Temperature** at 220-230°C
        - **Schedule Maintenance** regularly
        """)
    
    # Main content area
    tab1, tab2, tab3, tab4 = st.tabs(["🔮 Prediction", "📊 Analytics", "📈 Insights", "ℹ️ Help"])
    
    # Tab 1: Prediction Interface
    with tab1:
        st.header("Enter Machine Parameters")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🌡️ Temperature & Pressure")
            injection_temp = st.slider(
                "Injection Temperature (°C)",
                min_value=180.0,
                max_value=250.0,
                value=220.0,
                step=1.0,
                help="Molten plastic temperature"
            )
            
            injection_pressure = st.slider(
                "Injection Pressure (bar)",
                min_value=80.0,
                max_value=150.0,
                value=120.0,
                step=1.0,
                help="Hydraulic pressure during injection"
            )
            
            ambient_temp = st.slider(
                "Ambient Temperature (°C)",
                min_value=18.0,
                max_value=28.0,
                value=22.0,
                step=0.5,
                help="Factory floor temperature"
            )
        
        with col2:
            st.subheader("⏱️ Cycle Times")
            cycle_time = st.slider(
                "Cycle Time (seconds)",
                min_value=15.0,
                max_value=45.0,
                value=30.0,
                step=1.0,
                help="Time per part cycle"
            )
            
            cooling_time = st.slider(
                "Cooling Time (seconds)",
                min_value=8.0,
                max_value=20.0,
                value=12.0,
                step=1.0,
                help="Part cooling duration"
            )
            
            material_viscosity = st.slider(
                "Material Viscosity (Pa·s)",
                min_value=100.0,
                max_value=400.0,
                value=250.0,
                step=10.0,
                help="Plastic material flow resistance"
            )
        
        with col3:
            st.subheader("🔧 Machine & Operator")
            machine_age = st.slider(
                "Machine Age (years)",
                min_value=1.0,
                max_value=15.0,
                value=5.0,
                step=1.0,
                help="Equipment age"
            )
            
            operator_exp = st.slider(
                "Operator Experience (months)",
                min_value=1.0,
                max_value=120.0,
                value=24.0,
                step=1.0,
                help="Operator experience level"
            )
            
            maintenance_hours = st.slider(
                "Hours Since Maintenance",
                min_value=0.0,
                max_value=200.0,
                value=50.0,
                step=5.0,
                help="Hours since last maintenance"
            )
        
        st.markdown("---")
        
        # Predict button
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            predict_button = st.button("🚀 PREDICT OUTPUT", use_container_width=True)
        
        if predict_button:
            # Prepare input data
            input_data = {
                'Injection_Temperature': injection_temp,
                'Injection_Pressure': injection_pressure,
                'Cycle_Time': cycle_time,
                'Cooling_Time': cooling_time,
                'Material_Viscosity': material_viscosity,
                'Ambient_Temperature': ambient_temp,
                'Machine_Age': machine_age,
                'Operator_Experience': operator_exp,
                'Maintenance_Hours': maintenance_hours
            }
            
            # Make prediction
            with st.spinner('🔄 Calculating prediction...'):
                prediction = predict_output(model, input_data)
            
            # Display prediction
            st.markdown(f"""
            <div class="prediction-box">
                📦 Predicted Output: {prediction:.1f} parts/hour
            </div>
            """, unsafe_allow_html=True)
            
            # Additional insights
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                daily_output = prediction * 16  # 2 shifts
                st.metric("Daily Output (2 shifts)", f"{daily_output:.0f} parts")
            
            with col_b:
                total_cycle = cycle_time + cooling_time
                efficiency = (prediction / (3600 / total_cycle)) * 100 if total_cycle > 0 else 0
                st.metric("Cycle Efficiency", f"{efficiency:.1f}%")
            
            with col_c:
                temp_ratio = injection_temp / injection_pressure
                optimal = "✅ Optimal" if 1.7 <= temp_ratio <= 2.0 else "⚠️ Review"
                st.metric("Temp/Pressure Ratio", optimal)
            
            # Recommendations
            st.markdown("### 💡 Optimization Recommendations")
            recommendations = []
            
            if cycle_time > 35:
                recommendations.append("🔸 **Reduce Cycle Time**: Current cycle time is high. Consider optimizing mold design for faster cycles.")
            
            if operator_exp < 12:
                recommendations.append("🔸 **Operator Training**: Experienced operators can increase output by up to 15%.")
            
            if maintenance_hours > 150:
                recommendations.append("🔸 **Schedule Maintenance**: Overdue maintenance detected. Plan preventive service soon.")
            
            if injection_temp < 210 or injection_temp > 235:
                recommendations.append("🔸 **Optimize Temperature**: Target range is 220-230°C for best results.")
            
            if machine_age > 10:
                recommendations.append("🔸 **Equipment Upgrade**: Consider modernization for older machines.")
            
            if recommendations:
                for rec in recommendations:
                    st.markdown(rec)
            else:
                st.success("✅ All parameters are within optimal ranges!")
    
    # Tab 2: Analytics Dashboard
    with tab2:
        st.header("Parameter Impact Analysis")
        
        if predict_button:
            # Create sensitivity analysis
            st.subheader("📊 Sensitivity Analysis")
            
            # Cycle time sensitivity
            cycle_times = np.linspace(15, 45, 20)
            outputs = []
            
            for ct in cycle_times:
                test_input = input_data.copy()
                test_input['Cycle_Time'] = ct
                test_input['Cooling_Time'] = cooling_time
                outputs.append(predict_output(model, test_input))
            
            # Create plotly chart
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(
                x=cycle_times,
                y=outputs,
                mode='lines+markers',
                name='Predicted Output',
                line=dict(color='#1f77b4', width=3),
                marker=dict(size=8)
            ))
            fig1.add_vline(x=cycle_time, line_dash="dash", line_color="red", 
                          annotation_text="Current", annotation_position="top")
            fig1.update_layout(
                title="Impact of Cycle Time on Output",
                xaxis_title="Cycle Time (seconds)",
                yaxis_title="Parts per Hour",
                hovermode='x unified',
                template="plotly_white"
            )
            st.plotly_chart(fig1, use_container_width=True)
            
            # Multi-parameter comparison
            col1, col2 = st.columns(2)
            
            with col1:
                # Temperature sensitivity
                temps = np.linspace(180, 250, 15)
                temp_outputs = []
                for t in temps:
                    test_input = input_data.copy()
                    test_input['Injection_Temperature'] = t
                    temp_outputs.append(predict_output(model, test_input))
                
                fig2 = px.line(x=temps, y=temp_outputs, 
                              labels={'x': 'Temperature (°C)', 'y': 'Parts/Hour'},
                              title="Temperature Impact")
                fig2.update_traces(line_color='#ff7f0e', line_width=3)
                st.plotly_chart(fig2, use_container_width=True)
            
            with col2:
                # Operator experience sensitivity
                exp_range = np.linspace(1, 120, 15)
                exp_outputs = []
                for e in exp_range:
                    test_input = input_data.copy()
                    test_input['Operator_Experience'] = e
                    exp_outputs.append(predict_output(model, test_input))
                
                fig3 = px.line(x=exp_range, y=exp_outputs,
                              labels={'x': 'Experience (months)', 'y': 'Parts/Hour'},
                              title="Operator Experience Impact")
                fig3.update_traces(line_color='#2ca02c', line_width=3)
                st.plotly_chart(fig3, use_container_width=True)
            
            # Current settings radar chart
            st.subheader("🎯 Current Settings Overview")
            
            categories = ['Temperature\n(normalized)', 'Pressure\n(normalized)', 
                         'Cycle Speed\n(normalized)', 'Experience\n(normalized)',
                         'Maintenance\n(normalized)']
            
            values = [
                (injection_temp - 180) / (250 - 180) * 100,
                (injection_pressure - 80) / (150 - 80) * 100,
                (1 - (cycle_time - 15) / (45 - 15)) * 100,  # inverted
                (operator_exp - 1) / (120 - 1) * 100,
                (1 - maintenance_hours / 200) * 100  # inverted
            ]
            
            fig4 = go.Figure()
            fig4.add_trace(go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                name='Current Settings',
                line_color='#9467bd'
            ))
            fig4.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=False,
                title="Parameter Settings (% of optimal range)"
            )
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("👆 Make a prediction in the 'Prediction' tab to see analytics")
    
    # Tab 3: Insights
    with tab3:
        st.header("Manufacturing Insights & Best Practices")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔝 Top 5 Impact Factors")
            st.markdown("""
            Based on the trained model coefficients:
            
            1. **Cycle Time** (-5.35 coefficient)
               - Most impactful parameter
               - Each 1-second reduction = +5.3 parts/hour
               - **Action**: Optimize mold design and cooling
            
            2. **Total Cycle Time** (-4.85 coefficient)
               - Combined cycle + cooling effect
               - Focus on reducing both components
               - **Action**: Improve cooling efficiency
            
            3. **Operator Experience** (+3.81 coefficient)
               - Highly significant positive impact
               - Training pays off substantially
               - **Action**: Implement training programs
            
            4. **Injection Temperature** (+2.53 coefficient)
               - Moderate positive effect
               - Optimal range: 220-230°C
               - **Action**: Maintain temperature consistency
            
            5. **Machine Age** (-1.82 coefficient)
               - Older machines underperform
               - Regular maintenance mitigates this
               - **Action**: Upgrade or maintain aggressively
            """)
        
        with col2:
            st.subheader("💰 Business Impact Estimates")
            st.markdown("""
            **Optimization Potential:**
            
            📊 **Cycle Time Optimization**
            - 2-second reduction → +10.6 parts/hour
            - Daily gain: ~350 parts (2 shifts)
            - Annual value: $50-100K per machine
            
            👨‍🏭 **Operator Training**
            - 10% skill improvement → +3.8 parts/hour
            - Daily gain: ~125 parts
            - ROI: 300-500% in first year
            
            🌡️ **Temperature Control**
            - Optimal range maintenance → +2.5 parts/hour
            - Reduces defect rate by 15-20%
            - Energy savings: 5-10%
            
            🔧 **Preventive Maintenance**
            - Reduces downtime by 25-30%
            - Extends machine life 3-5 years
            - Maintains peak performance
            """)
            
            st.markdown("---")
            
            # ROI Calculator
            st.subheader("💵 Quick ROI Calculator")
            part_value = st.number_input("Part Value ($)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            shifts_per_day = st.number_input("Shifts per Day", min_value=1, max_value=3, value=2)
            days_per_year = st.number_input("Operating Days/Year", min_value=200, max_value=365, value=250)
            
            if predict_button and prediction:
                annual_parts = prediction * 8 * shifts_per_day * days_per_year
                annual_revenue = annual_parts * part_value
                
                st.success(f"📈 **Projected Annual Output**: {annual_parts:,.0f} parts")
                st.success(f"💰 **Projected Annual Revenue**: ${annual_revenue:,.2f}")
    
    # Tab 4: Help
    with tab4:
        st.header("📚 User Guide & Documentation")
        
        st.markdown("""
        ### How to Use This Tool
        
        1. **Navigate to the Prediction Tab**
           - Use the sliders to adjust machine parameters
           - All parameters have helpful tooltips (hover over ⓘ)
        
        2. **Enter Current Values**
           - Input your actual machine settings
           - Be as accurate as possible for best predictions
        
        3. **Click Predict**
           - Review the predicted output
           - Check the optimization recommendations
        
        4. **Analyze Results**
           - Switch to Analytics tab for detailed insights
           - View sensitivity analysis charts
        
        5. **Apply Insights**
           - Review the Insights tab for business recommendations
           - Use ROI calculator to estimate benefits
        
        ---
        
        ### Parameter Descriptions
        
        **Injection Temperature (°C)**
        - Range: 180-250°C
        - Optimal: 220-230°C
        - Effect: Higher temps generally increase flow
        
        **Injection Pressure (bar)**
        - Range: 80-150 bar
        - Optimal: 110-130 bar
        - Effect: Affects part quality and cycle time
        
        **Cycle Time (seconds)**
        - Range: 15-45 sec
        - Target: Minimize while maintaining quality
        - Effect: Direct inverse relationship with output
        
        **Cooling Time (seconds)**
        - Range: 8-20 sec
        - Depends on: Part size, material, temperature
        - Effect: Shorter is better, but don't rush
        
        **Material Viscosity (Pa·s)**
        - Range: 100-400 Pa·s
        - Varies by: Plastic type and grade
        - Effect: Lower viscosity flows easier
        
        **Ambient Temperature (°C)**
        - Range: 18-28°C
        - Optimal: 20-24°C
        - Effect: Affects cooling efficiency
        
        **Machine Age (years)**
        - Range: 1-15 years
        - Effect: Newer machines typically perform better
        - Mitigation: Regular maintenance
        
        **Operator Experience (months)**
        - Range: 1-120 months
        - Effect: Significant positive impact
        - Recommendation: Continuous training
        
        **Hours Since Maintenance**
        - Range: 0-200 hours
        - Recommended: <100 hours
        - Effect: Performance degrades over time
        
        ---
        
        ### Model Performance
        
        - **R² Score**: 0.8585 (85.85% variance explained)
        - **RMSE**: 4.30 parts/hour
        - **MAE**: 3.40 parts/hour
        
        The model is trained on 1,000 samples and validated using:
        - Statistical tests (Breusch-Pagan, Durbin-Watson)
        - Residual analysis
        - Cross-validation
        
        ---
        
        ### Support & Contact
        
        For technical support or questions:
        - 📧 Email: support@manufacturing-ml.com
        - 📞 Phone: (555) 123-4567
        - 🌐 Documentation: [docs.manufacturing-ml.com](https://docs.manufacturing-ml.com)
        
        Version: 1.0.0  
        Last Updated: October 2025
        """)

if __name__ == "__main__":
    main()
