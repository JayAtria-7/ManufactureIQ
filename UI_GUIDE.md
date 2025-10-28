# 🎨 Manufacturing Output Predictor - Web UI Guide

## 🚀 Quick Start

### Launch the Application

```cmd
# From the project root directory
venv\Scripts\activate
streamlit run app\streamlit_app.py
```

The UI will automatically open in your browser at `http://localhost:8501`

## 📱 User Interface Overview

### Main Features

The application has **4 main tabs**:

#### 1. 🔮 Prediction Tab
**Purpose**: Make real-time predictions

**How to Use:**
1. Adjust the sliders to match your current machine settings
2. All parameters have tooltips (hover over ⓘ for help)
3. Click "🚀 PREDICT OUTPUT" button
4. View:
   - Predicted parts per hour (large display)
   - Daily output estimate (2 shifts)
   - Cycle efficiency percentage
   - Temperature/Pressure ratio status
   - Automated optimization recommendations

**Tips:**
- Start with default values to see baseline performance
- Adjust one parameter at a time to see isolated impact
- Green checkmarks indicate optimal settings

#### 2. 📊 Analytics Tab
**Purpose**: Deep dive into parameter impacts

**Features:**
- **Sensitivity Charts**: See how changing each parameter affects output
- **Cycle Time Impact**: Interactive graph showing cycle time vs output
- **Temperature Impact**: Effect of temperature on production
- **Operator Experience**: ROI of training programs
- **Radar Chart**: Visual overview of all current settings

**How to Read Charts:**
- Blue line = predicted output
- Red dashed line = your current setting
- Higher output is better
- Look for steep slopes to identify high-impact parameters

#### 3. 📈 Insights Tab
**Purpose**: Business intelligence and recommendations

**Sections:**
- **Top 5 Impact Factors**: Ranked list with coefficients
- **Business Impact Estimates**: Dollar value of improvements
- **ROI Calculator**: Custom calculations for your operation
  - Enter part value, shifts, and days
  - Get annual output and revenue projections

**Action Items:**
1. Review top impact factors
2. Calculate ROI for proposed changes
3. Prioritize improvements by business value

#### 4. ℹ️ Help Tab
**Purpose**: Documentation and support

**Contents:**
- Step-by-step usage guide
- Detailed parameter descriptions with optimal ranges
- Model performance metrics
- Contact information

---

## 🎯 Common Use Cases

### Use Case 1: Optimize Current Production
**Goal**: Find best settings for maximum output

**Steps:**
1. Go to **Prediction** tab
2. Enter your current machine parameters
3. Click Predict
4. Review recommendations
5. Switch to **Analytics** tab
6. Identify which parameter has steepest impact
7. Adjust that parameter in small increments
8. Re-predict until you find optimal output

**Example:**
```
Current: Cycle Time = 35 sec, Output = 32 parts/hr
Optimization: Reduce to 28 sec
New Output: 42 parts/hr (+31% improvement!)
```

### Use Case 2: Compare Machine Configurations
**Goal**: Decide between equipment options

**Steps:**
1. Enter Machine A settings → Predict → Note output
2. Enter Machine B settings → Predict → Note output
3. Go to **Insights** → Use ROI calculator
4. Compare annual revenue projections
5. Make data-driven purchase decision

### Use Case 3: Training Impact Assessment
**Goal**: Justify operator training investment

**Steps:**
1. Prediction tab: Set experience = 6 months (current)
2. Note output (e.g., 30 parts/hr)
3. Change experience = 24 months (after training)
4. Note new output (e.g., 34 parts/hr)
5. Insights tab: Calculate annual revenue difference
6. Compare to training cost → ROI!

### Use Case 4: Maintenance Scheduling
**Goal**: Determine optimal maintenance intervals

**Steps:**
1. Set Maintenance Hours = 50 → Predict
2. Set Maintenance Hours = 150 → Predict
3. Note output degradation
4. Analytics tab: View sensitivity to maintenance
5. Find point where output drops significantly
6. Schedule maintenance before that point

---

## 💡 Pro Tips

### Getting the Most Accurate Predictions

1. **Be Precise**: Use actual measured values, not estimates
2. **Update Regularly**: Machine characteristics change over time
3. **Consider Context**: Model assumes normal operating conditions
4. **Validate**: Compare predictions to actual output initially

### Interpreting Results

**High Confidence Predictions:**
- Settings within trained ranges (shown in sliders)
- Similar to typical operating conditions
- All parameters within "green zone"

**Lower Confidence:**
- Extreme parameter values
- Unusual combinations
- Settings outside normal ranges

### Optimization Strategy

**Quick Wins (Immediate Impact):**
1. Reduce cycle time by 2-3 seconds
2. Optimize injection temperature to 220-230°C
3. Schedule overdue maintenance

**Medium-Term (3-6 months):**
1. Operator training programs
2. Process standardization
3. Equipment calibration

**Long-Term (6-12 months):**
1. Equipment upgrades for older machines
2. Advanced cooling systems
3. Automation enhancements

---

## 🎨 UI Color Coding

| Color | Meaning |
|-------|---------|
| 🟢 Green | Optimal range or good performance |
| 🟡 Yellow | Acceptable but could improve |
| 🔴 Red | Needs attention or out of range |
| 🔵 Blue | Information or neutral |
| 🟣 Purple | Predictions and analytics |

---

## 📊 Understanding the Charts

### Sensitivity Analysis Charts
- **X-axis**: Parameter value
- **Y-axis**: Predicted output (parts/hour)
- **Slope**: How much impact the parameter has
  - Steep slope = high impact
  - Flat slope = low impact
  - Negative slope = inverse relationship

### Radar Chart
- Shows all 5 parameters normalized to 0-100%
- Larger area = more optimal overall settings
- Look for balanced shape
- Sharp points indicate extreme values

---

## ⚠️ Troubleshooting

### Problem: "Model not loaded" error
**Solution**: 
1. Ensure you've run the Jupyter notebook first
2. Check that `models/model_pipeline.pkl` exists
3. Verify file paths are correct

### Problem: Predictions seem wrong
**Solution**:
1. Check all input values are reasonable
2. Ensure units are correct (°C, bar, seconds, etc.)
3. Verify you're within typical operating ranges

### Problem: Slow performance
**Solution**:
1. Close other applications
2. Reduce browser zoom if needed
3. Analytics tab calculations may take 2-3 seconds

### Problem: Charts not displaying
**Solution**:
1. Refresh the page (F5)
2. Ensure internet connection (for some chart libraries)
3. Try different browser (Chrome recommended)

---

## 🔧 Advanced Features

### Keyboard Shortcuts
- `R`: Rerun the application
- `C`: Clear cache
- `S`: Navigate to Settings (Streamlit menu)

### URL Parameters
You can bookmark specific configurations:
```
http://localhost:8501/?cycle_time=30&temp=220
```

### Export Data
- Charts can be downloaded (click camera icon)
- Right-click charts → "Save image as..."

---

## 📞 Support

**Technical Issues:**
- Check the Help tab in the application
- Review this guide
- Contact: support@manufacturing-ml.com

**Feature Requests:**
- Submit via the feedback form in Settings menu
- Email: features@manufacturing-ml.com

**Training:**
- Schedule a demo: training@manufacturing-ml.com
- Video tutorials: docs.manufacturing-ml.com/videos

---

## 🆕 What's New

### Version 1.0.0 (October 2025)
- ✅ Initial release
- ✅ Interactive prediction interface
- ✅ Real-time analytics
- ✅ ROI calculator
- ✅ Sensitivity analysis
- ✅ Automated recommendations

### Coming Soon
- 🔄 Batch predictions (upload CSV)
- 📧 Email reports
- 🔔 Alert notifications
- 📱 Mobile app
- 🤖 Auto-optimization suggestions

---

**Enjoy optimizing your manufacturing output! 🏭📈**
