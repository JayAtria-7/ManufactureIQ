# 🏭 ManufactureIQ - Final Comprehensive Documentation

**Last Updated:** October 28, 2025  
**Version:** 2.0.0 Enterprise  
**Project Status:** Production Ready  
**Author:** Jay Prakash Kumar  
**GitHub:** https://github.com/JayAtria-7/ManufactureIQ

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Features and Functionality](#2-features-and-functionality)
3. [Architecture and Design](#3-architecture-and-design)
4. [Frontend Documentation](#4-frontend-documentation)
5. [Backend Documentation](#5-backend-documentation)
6. [Database and Models](#6-database-and-models)
7. [Installation and Setup](#7-installation-and-setup)
8. [Running the Application](#8-running-the-application)
9. [Testing](#9-testing)
10. [Deployment](#10-deployment)
11. [Configuration](#11-configuration)
12. [Dependencies](#12-dependencies)
13. [Security Considerations](#13-security-considerations)
14. [Performance Optimization](#14-performance-optimization)
15. [Troubleshooting](#15-troubleshooting)
16. [Contributing Guidelines](#16-contributing-guidelines)
17. [Future Enhancements](#17-future-enhancements)
18. [Credits and References](#18-credits-and-references)

---

## 1. Project Overview

### 1.1 Project Name & Description

**ManufactureIQ** is an enterprise-grade AI-powered predictive analytics platform designed to optimize manufacturing operations through intelligent output prediction and machine learning analysis.

### 1.2 Purpose

ManufactureIQ leverages advanced machine learning models to:
- **Predict manufacturing output** (parts per hour) based on operational parameters
- **Optimize production workflows** with actionable insights
- **Reduce operational inefficiencies** through data-driven recommendations
- **Enable real-time decision making** for manufacturing teams
- **Provide enterprise-grade analytics** with beautiful, intuitive interfaces

### 1.3 Problem Statement & Solution

**Problem:**
- Manufacturing facilities lack real-time visibility into production capacity
- Manual production forecasting is inefficient and error-prone
- No data-driven approach to optimize operational parameters
- Difficult to identify factors impacting production output

**Solution:**
- Built a Linear Regression model trained on 1,000 manufacturing data samples
- Model achieves **R² = 0.859** (85.9% variance explained)
- Created an intuitive web interface for predictions and analysis
- Provided actionable insights for production optimization

### 1.4 Target Audience & Use Cases

**Primary Users:**
- Manufacturing plant managers
- Production planners
- Operations engineers
- Data analysts in manufacturing sector

**Key Use Cases:**
1. **Production Capacity Planning** - Forecast daily/weekly output
2. **Parameter Optimization** - Identify best settings for maximum throughput
3. **Predictive Maintenance** - Correlate machine age with output degradation
4. **Workforce Management** - Analyze operator experience impact on production
5. **Quality Assurance** - Optimize temperature and pressure parameters

### 1.5 Tech Stack Summary

| Layer | Technology | Version |
|-------|-----------|---------|
| **Frontend** | Streamlit | 1.50.0 |
| **Backend** | FastAPI | Latest |
| **ML Framework** | scikit-learn | 1.7.2 |
| **Data Processing** | pandas, numpy | Latest |
| **Visualization** | Plotly | 6.3.1 |
| **Runtime** | Python | 3.13.1 |
| **Server** | Uvicorn | Latest |
| **Deployment** | Streamlit Cloud, Docker | - |
| **Version Control** | Git | - |

---

## 2. Features and Functionality

### 2.1 Core Features

#### **Prediction Engine**
- Real-time manufacturing output prediction
- Accepts 9 operational parameters as input
- Returns predicted parts per hour with 85.9% accuracy
- Calculates derived features automatically

#### **Interactive Dashboard**
- Beautiful, responsive web interface
- 4 main tabs: Prediction, Analytics, Business Insights, Help
- Real-time statistics and KPI cards
- Professional corporate branding

#### **Advanced Analytics**
- **Parameter Impact Analysis** - Visualize how each parameter affects output
- **Sensitivity Analysis** - Compare actual vs. predicted values
- **Statistical Insights** - Distribution analysis and relationships
- **Correlation Matrix** - Feature interdependencies

#### **Business Intelligence**
- **ROI Calculator** - Calculate return on investment for optimizations
- **Efficiency Benchmarking** - Compare current vs. optimal settings
- **Production Recommendations** - AI-generated optimization suggestions
- **Trend Analysis** - Historical performance patterns

#### **User Experience Features**
- Animated prediction boxes with pulse effects
- Smooth transitions and hover effects
- Professional sidebar with company branding
- Responsive design for all screen sizes
- Dark/light mode support ready
- Mobile-friendly interface

### 2.2 Complete Feature Inventory

| Feature | Status | Description |
|---------|--------|-------------|
| Real-time Prediction | ✅ | Generates output predictions instantly |
| Analytics Dashboard | ✅ | Comprehensive parameter analysis |
| ROI Calculator | ✅ | Business impact calculations |
| Sensitivity Analysis | ✅ | Parameter impact visualization |
| Business Insights | ✅ | Actionable recommendations engine |
| REST API | ✅ | FastAPI backend for integrations |
| Streamlit UI v1.0 | ✅ | Original basic interface |
| Streamlit UI v2.0 | ✅ | Enhanced professional interface (Current) |
| Docker Support | ✅ | Containerized deployment |
| Cloud Deployment | ✅ | Streamlit Cloud ready |
| Footer Branding | ✅ | Personal portfolio footer with social links |
| Help System | ✅ | Comprehensive in-app documentation |

### 2.3 User Workflows

#### **Workflow 1: Quick Prediction**
1. User enters operational parameters in Prediction tab
2. System calculates derived features (Temperature/Pressure ratio, Total cycle time)
3. ML model generates prediction
4. Results displayed with confidence metrics
5. User can adjust parameters to see impact

#### **Workflow 2: Optimization Analysis**
1. User navigates to Analytics tab
2. Selects parameters to analyze
3. Views correlation matrix and impact charts
4. Identifies optimization opportunities
5. Reviews recommendations

#### **Workflow 3: Business Planning**
1. User goes to Business Insights tab
2. Uses ROI calculator for investment scenarios
3. Views efficiency comparisons
4. Downloads recommendations report
5. Makes data-driven decisions

### 2.4 Business Logic

#### **Prediction Logic**
```python
# Derived Features Calculated Automatically:
- Temperature_Pressure_Ratio = Injection_Temperature / Injection_Pressure
- Total_Cycle_Time = Cycle_Time + Cooling_Time
- hour = Current hour of day (for temporal patterns)
- is_weekend = Whether current day is weekend (0 or 1)

# Prediction Formula:
output = trained_linear_regression_model.predict(features)
```

#### **Feature Importance (Top 5)**
1. **Cycle_Time** (Coefficient: -5.35) - Most impactful
2. **Total_Cycle_Time** (Coefficient: -4.85)
3. **Operator_Experience** (Coefficient: +3.81)
4. **Injection_Temperature** (Coefficient: +2.53)
5. **Machine_Age** (Coefficient: -1.82)

---

## 3. Architecture and Design

### 3.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Client Layer                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Streamlit    │  │   FastAPI    │  │   Docker     │      │
│  │ UI v1.0      │  │   REST API   │  │ Container    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Business Logic Layer                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Model Inference Pipeline                            │   │
│  │  - Preprocessing                                     │   │
│  │  - Feature Engineering                               │   │
│  │  - Model Prediction                                  │   │
│  │  - Post-processing                                   │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Data Layer                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Model Files  │  │ Metadata     │  │ Training     │      │
│  │ (.pkl)       │  │ (.json)      │  │ Data (.csv)  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 System Design Patterns

- **MVC Pattern** - Streamlit handles View and Controller
- **Repository Pattern** - Model artifacts stored in `models/` directory
- **Factory Pattern** - Model pipeline instantiation
- **Singleton Pattern** - Lazy loading of ML models to optimize memory

### 3.3 Project Folder Structure

```
ManufactureIQ/
├── app/
│   ├── main.py                          # FastAPI backend application
│   ├── streamlit_app.py                 # Streamlit UI v1.0 (basic)
│   ├── streamlit_app_v2.py              # Streamlit UI v2.0 (enhanced)
│   └── __pycache__/
│
├── models/
│   ├── model_pipeline.pkl               # Trained LinearRegression model
│   ├── preprocessor.pkl                 # Standalone preprocessor
│   └── metadata.json                    # Model metrics & features
│
├── .streamlit/
│   └── config.toml                      # Streamlit configuration
│
├── .devcontainer/                       # VS Code dev container config
├── .dockerignore                        # Docker ignore rules
├── .gitignore                           # Git ignore rules
├── Dockerfile                           # Docker containerization
│
├── CapstoneProject1LR.ipynb             # Data science notebook
├── capstone_manufacturing_lr.ipynb      # Training notebook
├── manufacturing_dataset_1000_samples.csv # Training dataset
│
├── requirements.txt                     # Python dependencies (all)
├── requirements_streamlit.txt           # Dependencies for Streamlit
│
├── run_ui.bat                           # Batch script for UI v1.0
├── run_ui_v2.bat                        # Batch script for UI v2.0
├── test_api.py                          # API endpoint testing script
│
├── README.md                            # Quick start guide
├── DEPLOYMENT_GUIDE.md                  # Detailed deployment guide
├── DEPLOYMENT_CHECKLIST.md              # Pre-deployment checklist
├── STREAMLIT_CLOUD_DEPLOYMENT.md        # Cloud-specific guide
├── V2_RELEASE_NOTES.md                  # v2.0 feature notes
├── UI_GUIDE.md                          # User guide for UI
├── VISUAL_COMPARISON.md                 # v1.0 vs v2.0 comparison
├── BUG_FIX_COLUMN_NAME.md               # Bug fix documentation
├── FINAL_COMPREHENSIVE_DOCUMENTATION.md # This file
│
└── venv/                                # Python virtual environment
```

### 3.4 Component Relationships

```
┌─────────────────────────────────────────┐
│     User Interface (Streamlit)          │
│  ┌───────────────────────────────────┐  │
│  │ Prediction Tab                    │  │
│  │ - Input parameters                │  │
│  │ - Call inference pipeline         │  │
│  │ - Display results                 │  │
│  └───────────────────────────────────┘  │
│  ┌───────────────────────────────────┐  │
│  │ Analytics Tab                     │  │
│  │ - Statistical analysis            │  │
│  │ - Correlation matrices            │  │
│  │ - Sensitivity analysis            │  │
│  └───────────────────────────────────┘  │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │  Model Pipeline     │
        │  (model_pipeline.pkl)
        │  - Preprocessor     │
        │  - LinearRegression │
        └──────────┬──────────┘
                   │
        ┌──────────▼────────────────┐
        │  Metadata                 │
        │  (metadata.json)          │
        │  - Features list          │
        │  - Model metrics          │
        │  - Random state           │
        └───────────────────────────┘
```

---

## 4. Frontend Documentation

### 4.1 Framework and Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| **Streamlit** | 1.50.0 | Web framework & UI components |
| **Plotly** | 6.3.1 | Interactive visualizations |
| **pandas** | Latest | Data manipulation |
| **numpy** | Latest | Numerical operations |
| **streamlit.components.v1** | Built-in | Custom HTML rendering |

### 4.2 UI/UX Components Inventory

#### **Header Components**
- **Company Header** - Gradient background, company logo, tagline
- **Quick Stats Banner** - 4 metric cards (Real-Time, Accuracy, Parameters, AI-Powered)

#### **Tab Components**
- **Prediction Tab** - Input form, prediction display, metrics
- **Analytics Tab** - Charts, analysis, statistics
- **Business Insights Tab** - ROI calculator, recommendations
- **Help Tab** - Documentation, support info, FAQs

#### **Card Components**
- **Info Card** - Statistics display with icons
- **Metric Card** - KPI displays with styling
- **Sidebar Brand Card** - Company branding in sidebar

#### **Interactive Components**
- **Number Input** - Parameter entry fields
- **Button** - Prediction trigger
- **Slider** - Parameter adjustment (for sensitivity analysis)
- **Checkbox** - Feature selection
- **Radio** - Mode selection

#### **Display Components**
- **Success Box** - Prediction results display
- **Info Box** - Informational messages
- **Metric Display** - KPI visualization
- **Chart** - Plotly interactive graphs

### 4.3 State Management Approach

Streamlit uses session state for managing application state:

```python
# Initialize session state
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None

if 'input_parameters' not in st.session_state:
    st.session_state.input_parameters = {}

# Update state
st.session_state.prediction_result = new_prediction
st.session_state.input_parameters = user_inputs
```

### 4.4 Routing Structure

Streamlit implements single-page routing via tabs:
- **Tab 1: Prediction** - Main prediction interface
- **Tab 2: Analytics** - Detailed analysis and statistics
- **Tab 3: Business Insights** - ROI and recommendations
- **Tab 4: Help** - Documentation and support

### 4.5 Styling Methodology

#### **CSS Architecture**
- **Google Fonts** - Poppins (headings), Inter (body)
- **Color Scheme** - Blue gradient (#1e3a8a → #3b82f6 → #06b6d4)
- **Responsive Design** - Mobile-first approach
- **Animations** - Fade-in, pulse, hover effects

#### **Theme Configuration** (`config.toml`)
```toml
[theme]
primaryColor = "#3b82f6"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8fafc"
textColor = "#0f172a"
font = "sans serif"
```

#### **Custom Styling**
- Gradient backgrounds for headers
- Box shadows for depth
- Border radius for modern look
- Smooth transitions (0.3s ease)
- Pulse animations for emphasis

### 4.6 Key Pages/Views

#### **Page 1: Prediction Tab**
- **Purpose:** Real-time production output prediction
- **Components:**
  - 9 input fields for machine parameters
  - "Generate Prediction" button
  - Animated result display
  - Confidence metrics
- **Logic:** Accepts inputs → calculates derived features → calls model → displays results

#### **Page 2: Analytics Tab**
- **Purpose:** Statistical analysis and insights
- **Components:**
  - Parameter correlation matrix
  - Feature importance chart
  - Distribution analysis
  - Statistical summary table
- **Logic:** Analyzes training data → generates visualizations → displays insights

#### **Page 3: Business Insights Tab**
- **Purpose:** Business-focused recommendations and ROI analysis
- **Components:**
  - ROI calculator
  - Efficiency metrics
  - Optimization recommendations
  - Cost-benefit analysis
- **Logic:** Compares scenarios → calculates ROI → generates recommendations

#### **Page 4: Help Tab**
- **Purpose:** Documentation and support
- **Components:**
  - FAQ section
  - Feature explanations
  - Support contact information
  - User guides
- **Logic:** Displays helpful information → provides support links

### 4.7 Frontend Environment Variables

```env
# Streamlit specific (none required - uses defaults)
# All configuration in .streamlit/config.toml
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

---

## 5. Backend Documentation

### 5.1 Server Framework & Runtime

- **Framework:** FastAPI (modern, fast, with automatic API documentation)
- **Server:** Uvicorn (ASGI server)
- **Runtime:** Python 3.13.1
- **Port:** 8000 (default)

### 5.2 API Architecture

**Type:** REST API  
**Base URL:** `http://localhost:8000`  
**Documentation:** Available at `/docs` (Swagger UI)

### 5.3 Complete API Endpoints

#### **1. Root Endpoint**
```
GET /
Response: {"message": "Manufacturing Output Predictor API", "status": "running"}
Purpose: Verify API is running
```

#### **2. Health Check Endpoint**
```
GET /health
Response: {
    "status": "ok",
    "model_loaded": true,
    "metadata_loaded": true
}
Purpose: Check API and model availability
```

#### **3. Metadata Endpoint**
```
GET /metadata
Response: {
    "train_metrics": {...},
    "test_metrics": {...},
    "feature_list": [...],
    "random_state": 42
}
Purpose: Get model metadata and performance metrics
```

#### **4. Prediction Endpoint** (Main)
```
POST /predict

Request Body (JSON):
{
    "Injection_Temperature": 220,
    "Injection_Pressure": 120,
    "Cycle_Time": 30,
    "Cooling_Time": 12,
    "Material_Viscosity": 250,
    "Ambient_Temperature": 22,
    "Machine_Age": 5,
    "Operator_Experience": 24,
    "Maintenance_Hours": 50
}

Response (JSON):
{
    "predicted_parts_per_hour": 45.8,
    "input": {...},
    "derived_features": {
        "Temperature_Pressure_Ratio": 1.833,
        "Total_Cycle_Time": 42
    }
}

Status Codes:
- 200: Successful prediction
- 400: Invalid input
- 503: Model not loaded
```

### 5.4 Authentication & Authorization

**Current Implementation:**
- No authentication required (suitable for internal use)
- All endpoints publicly accessible

**Production Recommendations:**
- Implement OAuth 2.0 or API key authentication
- Use JWT tokens for user sessions
- Implement rate limiting
- Add CORS restrictions

### 5.5 Middleware & Purposes

**Default Middleware:**
- **CORSMiddleware** - Cross-Origin Resource Sharing (if enabled)
- **TrustedHostMiddleware** - Host validation
- **HTTPSRedirectMiddleware** - HTTPS enforcement (production)

### 5.6 Database Schema & Models

#### **Pydantic Model: InputData**
```python
class InputData(BaseModel):
    Injection_Temperature: float    # °C
    Injection_Pressure: float       # bar
    Cycle_Time: float              # seconds
    Cooling_Time: float            # seconds
    Material_Viscosity: float       # cP (centipoise)
    Ambient_Temperature: float      # °C
    Machine_Age: float             # years
    Operator_Experience: float     # years
    Maintenance_Hours: float       # hours
```

#### **Model Output Features**
```python
# Automatically calculated from inputs:
- Temperature_Pressure_Ratio (derived)
- Total_Cycle_Time (derived)
- hour (current hour, default: 12)
- is_weekend (default: 0)
```

### 5.7 Business Logic & Services

#### **Model Pipeline Architecture**
1. **Input Validation** - Pydantic model validation
2. **Derived Feature Calculation:**
   - `Temperature_Pressure_Ratio = Injection_Temp / Injection_Press`
   - `Total_Cycle_Time = Cycle_Time + Cooling_Time`
3. **DataFrame Construction** - Create pandas DataFrame with all 13 features
4. **Preprocessing** - Apply fitted preprocessor (scaler)
5. **Prediction** - Linear Regression model inference
6. **Response Formatting** - Return prediction with metadata

#### **Error Handling**
- 503 Service Unavailable: Model not loaded
- 500 Internal Server Error: Prediction computation error
- 400 Bad Request: Invalid input parameters

### 5.8 Backend Environment Variables

```env
# FastAPI specific
PYTHONUNBUFFERED=1

# Model paths
MODEL_PATH=models/model_pipeline.pkl
METADATA_PATH=models/metadata.json
```

---

## 6. Database and Models

### 6.1 Model Type & Version

- **Algorithm:** Linear Regression (scikit-learn)
- **Purpose:** Predict manufacturing output (parts/hour)
- **Training Data:** 1,000 samples from manufacturing operations
- **Model Version:** v1.0
- **Model Files:** 
  - `model_pipeline.pkl` (trained model + preprocessor)
  - `preprocessor.pkl` (standalone feature scaler)

### 6.2 Model Performance Metrics

#### **Test Set Performance:**
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| R² (Coefficient of Determination) | 0.859 | > 0.75 | ✅ Exceeds |
| RMSE (Root Mean Squared Error) | 4.30 parts/hour | < 5.0 | ✅ Good |
| MAE (Mean Absolute Error) | 3.40 parts/hour | < 4.0 | ✅ Good |

#### **Training Set Performance:**
| Metric | Value |
|--------|-------|
| R² | 0.869 |
| RMSE | 4.37 parts/hour |
| MAE | 3.29 parts/hour |

### 6.3 Feature Schema

#### **13 Features in Model** (Feature Order Critical)
| # | Feature | Type | Range | Unit | Notes |
|---|---------|------|-------|------|-------|
| 1 | Injection_Temperature | Float | 200-240 | °C | Controls material flow |
| 2 | Injection_Pressure | Float | 80-150 | bar | Force of injection |
| 3 | Cycle_Time | Float | 20-50 | sec | Per-part production time |
| 4 | Cooling_Time | Float | 5-20 | sec | Solidification time |
| 5 | Material_Viscosity | Float | 200-400 | cP | Material thickness |
| 6 | Ambient_Temperature | Float | 15-35 | °C | Room temperature |
| 7 | Machine_Age | Float | 1-15 | years | Equipment age |
| 8 | Operator_Experience | Float | 5-40 | years | Worker skill level |
| 9 | Maintenance_Hours | Float | 10-100 | hours | Equipment maintenance time |
| 10 | Temperature_Pressure_Ratio | Float | Derived | - | Injection_Temp / Injection_Press |
| 11 | Total_Cycle_Time | Float | Derived | - | Cycle_Time + Cooling_Time |
| 12 | hour | Integer | 0-23 | - | Hour of day (temporal) |
| 13 | is_weekend | Binary | 0-1 | - | Weekend indicator |

### 6.4 Feature Importance (Coefficients)

**Model Coefficients (sorted by impact magnitude):**

| Rank | Feature | Coefficient | Direction | Interpretation |
|------|---------|-------------|-----------|-----------------|
| 1 | Cycle_Time | -5.35 | Negative | Longer cycle → fewer parts/hour |
| 2 | Total_Cycle_Time | -4.85 | Negative | Extended production time → lower output |
| 3 | Operator_Experience | +3.81 | Positive | More experience → higher output |
| 4 | Injection_Temperature | +2.53 | Positive | Higher temp → better flow |
| 5 | Machine_Age | -1.82 | Negative | Older equipment → reduced capacity |
| 6 | Maintenance_Hours | +0.12 | Positive | Maintenance improves performance |
| 7 | Ambient_Temperature | -0.08 | Negative | Environmental effect (minimal) |
| 8 | Material_Viscosity | +0.01 | Positive | Minor impact |
| 9 | Cooling_Time | -0.01 | Negative | Minimal impact |
| 10 | Injection_Pressure | +0.002 | Positive | Negligible |
| 11 | Temperature_Pressure_Ratio | ~0 | - | Captured by components |
| 12 | hour | ~0 | - | No strong temporal pattern |
| 13 | is_weekend | ~0 | - | No shift difference |

### 6.5 Model Training & Validation

#### **Data Split:**
- Training Set: 80% (800 samples)
- Test Set: 20% (200 samples)
- Random State: 42 (reproducible)

#### **Preprocessing Pipeline:**
1. StandardScaler - Normalize all features to mean=0, std=1
2. Handles both raw and derived features

#### **Validation Approach:**
- Train/test split (time-independent)
- No cross-validation (simplicity)
- No regularization (L1/L2) - basic LinearRegression

### 6.6 Data Storage Location

```
models/
├── model_pipeline.pkl       # Complete model + preprocessor
├── preprocessor.pkl         # Standalone scaler
└── metadata.json           # Metrics, features, config
```

---

## 7. Installation and Setup

### 7.1 Prerequisites

| Requirement | Minimum | Recommended | Check |
|-------------|---------|-------------|-------|
| Python | 3.8 | 3.13.1 | `python --version` |
| pip | 20.0 | Latest | `pip --version` |
| Git | 2.0 | Latest | `git --version` |
| OS | Any | Windows/Linux/Mac | - |
| RAM | 2GB | 4GB+ | - |
| Storage | 500MB | 1GB+ | - |

### 7.2 Step-by-Step Local Setup

#### **Step 1: Clone Repository**
```bash
git clone https://github.com/JayAtria-7/ManufactureIQ.git
cd ManufactureIQ
```

#### **Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### **Step 3: Upgrade pip**
```bash
pip install --upgrade pip
```

#### **Step 4: Install Dependencies**

**Option A: Full Installation (All Features)**
```bash
pip install -r requirements.txt
```

**Option B: Streamlit Only**
```bash
pip install -r requirements_streamlit.txt
```

#### **Step 5: Verify Installation**
```bash
python -c "import streamlit, fastapi, pandas, numpy, plotly, sklearn; print('All packages installed successfully!')"
```

### 7.3 Environment Configuration

#### **.env Template** (Create if needed)
```env
# Optional: For cloud deployment
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
STREAMLIT_LOGGER_LEVEL=info

# Optional: API configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=false
```

#### **Streamlit Configuration** (`.streamlit/config.toml`)
```toml
[server]
headless = true

[theme]
primaryColor = "#3b82f6"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8fafc"
textColor = "#0f172a"
font = "sans serif"

[browser]
gatherUsageStats = false
```

### 7.4 Dependency Installation Commands

```bash
# Install all dependencies
pip install -r requirements.txt

# Install specific versions for Streamlit
pip install streamlit==1.50.0 plotly==6.3.1

# Install ML stack
pip install scikit-learn==1.7.2 pandas numpy joblib

# Install backend
pip install fastapi uvicorn pydantic

# Install development tools
pip install jupyter notebook ipykernel
```

### 7.5 Database Setup Instructions

**Note:** This project does not use a traditional database. Data is stored as:
- Model files (`.pkl`)
- Metadata (`.json`)
- Training data (`.csv`)

No database setup required!

---

## 8. Running the Application

### 8.1 Development Server Commands

#### **Option 1: Streamlit UI v2.0 (Recommended)**
```bash
streamlit run app/streamlit_app_v2.py
# Or use batch file:
run_ui_v2.bat
```
**Access:** http://localhost:8501

#### **Option 2: Streamlit UI v1.0 (Basic)**
```bash
streamlit run app/streamlit_app.py
# Or use batch file:
run_ui.bat
```
**Access:** http://localhost:8501

#### **Option 3: FastAPI Backend Only**
```bash
cd app
uvicorn main:app --reload --port 8000
# Or custom port:
uvicorn main:app --reload --port 8001
```
**Access:** http://localhost:8000  
**API Docs:** http://localhost:8000/docs (Swagger UI)

#### **Option 4: Jupyter Notebook**
```bash
jupyter notebook capstone_manufacturing_lr.ipynb
```

### 8.2 Build Commands

```bash
# Docker build
docker build -t manufacture-iq:latest .

# Docker run
docker run -p 8501:8501 manufacture-iq:latest
```

### 8.3 Testing Commands

```bash
# Test API endpoints
python test_api.py

# Or use curl
curl http://localhost:8000/health
```

### 8.4 Linting & Formatting Commands

```bash
# Format with black (if installed)
black app/*.py

# Lint with flake8 (if installed)
flake8 app/*.py
```

### 8.5 Available Scripts

| Script | Purpose | Command |
|--------|---------|---------|
| `run_ui.bat` | Launch Streamlit UI v1.0 | `run_ui.bat` |
| `run_ui_v2.bat` | Launch Streamlit UI v2.0 | `run_ui_v2.bat` |
| `test_api.py` | Test API endpoints | `python test_api.py` |

---

## 9. Testing

### 9.1 Testing Frameworks

- **Manual Testing:** Python test scripts
- **API Testing:** cURL, Postman, Python requests
- **UI Testing:** Manual browser testing

### 9.2 Test Coverage

**Current Coverage:**
- Model prediction accuracy: ✅ Tested
- API endpoints: ✅ Tested
- UI components: ✅ Manual tested
- Edge cases: ⚠️ Partial

### 9.3 How to Run Unit Tests

```bash
# Run test script
python test_api.py
```

### 9.4 How to Run Integration Tests

```bash
# Start Streamlit
streamlit run app/streamlit_app_v2.py

# In browser, manually test:
# 1. Enter parameters
# 2. Click "Generate Prediction"
# 3. Check results display
# 4. Navigate through tabs
# 5. Verify analytics work
```

### 9.5 Test File Locations

- `test_api.py` - API endpoint tests
- `capstone_manufacturing_lr.ipynb` - Model training and validation
- Model tests in notebook

---

## 10. Deployment

### 10.1 Deployment Platforms & Services

| Platform | Status | Cost | Recommendation |
|----------|--------|------|-----------------|
| **Streamlit Cloud** | ✅ Ready | Free | Recommended (easiest) |
| **Docker + AWS** | ✅ Ready | ~$10/month | For enterprise |
| **Heroku** | ✅ Compatible | $5-50/month | Beginner-friendly |
| **Azure** | ✅ Compatible | Variable | Enterprise option |
| **Local Server** | ✅ Ready | $0 (on-prem) | Development only |

### 10.2 Production Build Process

#### **Step 1: Prepare Files**
```bash
# Ensure files are ready
models/model_pipeline.pkl     ✅ Present
models/metadata.json          ✅ Present
app/streamlit_app_v2.py       ✅ Present
requirements_streamlit.txt    ✅ Present
.streamlit/config.toml        ✅ Present
```

#### **Step 2: Create .gitignore** (if not present)
```
venv/
__pycache__/
*.pyc
.DS_Store
.env
```

#### **Step 3: Push to GitHub**
```bash
git add .
git commit -m "Production ready: ManufactureIQ v2.0"
git push origin main
```

#### **Step 4: Deploy**
See section 10.3 for platform-specific steps

### 10.3 Environment-Specific Configurations

#### **Development**
```python
DEBUG = True
RELOAD = True
PORT = 8503
```

#### **Production**
```python
DEBUG = False
RELOAD = False
PORT = 8501
```

### 10.4 CI/CD Pipeline

**Current Setup:** Manual deployment  
**Recommended:** GitHub Actions

**Example GitHub Actions workflow:**
```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Streamlit Cloud
        run: |
          # Deployment script here
```

### 10.5 Deployment Commands & Steps

#### **Streamlit Cloud (Recommended)**

**Step 1:** Create GitHub repository
```bash
git push origin main
```

**Step 2:** Visit https://share.streamlit.io

**Step 3:** Click "New app"

**Step 4:** Configure deployment
```
Repository: JayAtria-7/ManufactureIQ
Branch: main
Main file path: app/streamlit_app_v2.py
```

**Step 5:** Click "Deploy"

**Step 6:** Wait 2-3 minutes for deployment

#### **Docker Deployment**
```bash
# Build image
docker build -t manufacture-iq:v2.0 .

# Run container
docker run -p 8501:8501 manufacture-iq:v2.0

# Push to Docker Hub (optional)
docker tag manufacture-iq:v2.0 jayatria7/manufacture-iq:v2.0
docker push jayatria7/manufacture-iq:v2.0
```

### 10.6 Domain & Hosting

- **Public URL:** https://share.streamlit.io/jayatria-7/manufactureiq/main/app/streamlit_app_v2.py (via Streamlit Cloud)
- **GitHub Repository:** https://github.com/JayAtria-7/ManufactureIQ
- **Domain:** (Set up custom domain if needed)

---

## 11. Configuration

### 11.1 All Environment Variables with Descriptions

| Variable | Value | Description | Required |
|----------|-------|-------------|----------|
| `STREAMLIT_SERVER_HEADLESS` | `true` | Run without UI for deployment | No |
| `STREAMLIT_BROWSER_GATHER_USAGE_STATS` | `false` | Disable usage analytics | No |
| `STREAMLIT_LOGGER_LEVEL` | `info` | Logging level | No |
| `PYTHONUNBUFFERED` | `1` | Real-time log output | No |
| `API_HOST` | `0.0.0.0` | FastAPI server host | No |
| `API_PORT` | `8000` | FastAPI server port | No |
| `DEBUG` | `false` | Debug mode (production) | No |

### 11.2 Configuration Files Explanations

#### **.streamlit/config.toml**
```toml
[server]
headless = true                    # Run without browser UI

[theme]
primaryColor = "#3b82f6"          # Main brand color
backgroundColor = "#ffffff"       # Page background
secondaryBackgroundColor = "#f8fafc"  # Card background
textColor = "#0f172a"             # Text color
font = "sans serif"               # Font family

[browser]
gatherUsageStats = false          # Disable tracking
```

#### **.gitignore** (Key entries)
```
venv/                             # Virtual environment
__pycache__/                      # Python cache
*.pyc                             # Compiled Python
.DS_Store                         # macOS files
.env                              # Secrets
.ipynb_checkpoints/               # Jupyter cache
```

#### **requirements.txt** (Key packages)
```
pandas==latest                    # Data manipulation
numpy==latest                     # Numerical computing
scikit-learn==1.7.2              # Machine learning
streamlit==1.50.0                # Web framework
plotly==6.3.1                    # Visualizations
fastapi==latest                  # API framework
```

### 11.3 API Keys & Secrets Management

**Current Status:** No API keys needed (public app)

**Production Recommendations:**
- Use environment variables for secrets
- Store in `.env` file (excluded from git)
- Use tools like `python-dotenv`

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
```

---

## 12. Dependencies

### 12.1 Major Dependencies with Purposes

| Package | Version | Purpose | License |
|---------|---------|---------|---------|
| **streamlit** | 1.50.0 | Web UI framework | Apache 2.0 |
| **plotly** | 6.3.1 | Interactive charts | MIT |
| **pandas** | Latest | Data manipulation | BSD 3 |
| **numpy** | Latest | Numerical computing | BSD 3 |
| **scikit-learn** | 1.7.2 | Machine learning | BSD 3 |
| **fastapi** | Latest | REST API framework | MIT |
| **uvicorn** | Latest | ASGI server | BSD 3 |
| **joblib** | Latest | Model serialization | BSD 3 |
| **pydantic** | Latest | Data validation | MIT |

### 12.2 Dev Dependencies

```
jupyter           # Interactive notebooks
notebook          # Jupyter notebook support
black             # Code formatter
flake8            # Linter
pytest            # Testing framework
```

### 12.3 Version Requirements & Compatibility

| Component | Requirement | Tested | Status |
|-----------|-------------|--------|--------|
| Python | >= 3.8 | 3.13.1 | ✅ Compatible |
| Streamlit | >= 1.0 | 1.50.0 | ✅ Latest |
| pandas | >= 1.0 | Latest | ✅ Compatible |
| scikit-learn | >= 1.0 | 1.7.2 | ✅ Latest |
| plotly | >= 5.0 | 6.3.1 | ✅ Latest |

---

## 13. Security Considerations

### 13.1 Authentication Implementation

**Current Status:** No authentication (suitable for demo/internal use)

**Production Recommendations:**
```python
from fastapi.security import HTTPBearer, HTTPAuthCredentials

security = HTTPBearer()

@app.post("/predict")
def predict(payload: InputData, credentials: HTTPAuthCredentials = Depends(security)):
    # Validate credentials
    token = credentials.credentials
    # Verify token...
```

### 13.2 Authorization Levels

**Current:** No role-based access control (RBAC)

**Recommended:**
- Admin: Full access
- User: Prediction + analytics only
- Guest: Read-only access

### 13.3 Data Validation

**Input Validation (Pydantic):**
```python
class InputData(BaseModel):
    Injection_Temperature: float      # Type validation
    Injection_Pressure: float         # Range validation possible
    # ... etc
```

**Recommended Additional Validation:**
```python
class InputData(BaseModel):
    Injection_Temperature: float = Field(..., ge=200, le=240)  # 200-240°C
    Injection_Pressure: float = Field(..., ge=80, le=150)      # 80-150 bar
    Cycle_Time: float = Field(..., ge=20, le=50)               # 20-50 sec
```

### 13.4 Security Best Practices Followed

✅ **Implemented:**
- Input validation (Pydantic)
- No hardcoded secrets
- Error message masking (limited detail)
- CORS disabled by default

⚠️ **Recommended:**
- HTTPS enforcement (production)
- Rate limiting (prevent abuse)
- API authentication (OAuth/JWT)
- Audit logging
- SQL injection prevention (N/A - no DB)

### 13.5 Known Vulnerabilities & Mitigations

| Vulnerability | Risk | Mitigation | Status |
|---------------|------|-----------|--------|
| Unauthorized API access | Low | Add authentication | ⏳ TODO |
| DDoS attacks | Medium | Rate limiting | ⏳ TODO |
| Data exposure | Low | HTTPS + encryption | ⏳ TODO |
| Model poisoning | Low | Validate training data | ✅ Done |
| Information disclosure | Low | Mask error details | ✅ Done |

---

## 14. Performance Optimization

### 14.1 Caching Strategies

#### **Streamlit Caching**
```python
@st.cache_data
def load_model():
    return joblib.load('models/model_pipeline.pkl')

@st.cache_resource
def get_metadata():
    with open('models/metadata.json') as f:
        return json.load(f)
```

#### **API Caching**
```python
# Use HTTP caching headers
@app.get("/metadata")
def get_metadata():
    return {
        "metadata": {...},
        "cache-control": "public, max-age=3600"
    }
```

### 14.2 Code Splitting (Streamlit)

- **Tab-based architecture** - Load only visible content
- **Lazy imports** - Import heavy libraries on demand
- **Component modularity** - Separate UI components into functions

### 14.3 Lazy Loading Implementations

```python
# Load model only when needed
if 'model' not in st.session_state:
    st.session_state.model = joblib.load('models/model_pipeline.pkl')

# Load charts only in Analytics tab
if tab == "Analytics":
    load_analytics_charts()
```

### 14.4 Performance Monitoring Tools

- **Streamlit Profiler** - Built-in performance tracking
- **Application Performance Monitoring (APM)** - Consider for production
- **Manual benchmarking** - Time critical functions

**Example Benchmark:**
```python
import time

start = time.time()
prediction = model.predict(X)
elapsed = time.time() - start
print(f"Prediction time: {elapsed:.3f}s")
```

---

## 15. Troubleshooting

### 15.1 Common Issues & Solutions

#### **Issue 1: "Column 'Material_Viscosity' is missing"**
**Cause:** Feature name mismatch in model training  
**Solution:** Ensure column names exactly match metadata.json  
**Fixed in:** v2.0.0

#### **Issue 2: Streamlit takes long time to load**
**Cause:** Model not cached, loading on every run  
**Solution:** Use `@st.cache_resource` decorator  
**Example:**
```python
@st.cache_resource
def load_model():
    return joblib.load('models/model_pipeline.pkl')
```

#### **Issue 3: "ModuleNotFoundError: No module named 'streamlit'"**
**Cause:** Dependencies not installed  
**Solution:** Run `pip install -r requirements_streamlit.txt`

#### **Issue 4: Port already in use (8501)**
**Cause:** Another Streamlit instance running  
**Solution:** 
```bash
streamlit run app/streamlit_app_v2.py --server.port 8503
```

#### **Issue 5: API not responding**
**Cause:** Uvicorn not started or port blocked  
**Solution:**
```bash
cd app
uvicorn main:app --reload --port 8000
```

#### **Issue 6: Model prediction returns NaN**
**Cause:** Invalid input parameters (out of range)  
**Solution:** Validate input ranges before sending

### 15.2 Debug Mode Instructions

#### **Streamlit Debug**
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Or via Streamlit
streamlit run app/streamlit_app_v2.py --logger.level=debug
```

#### **FastAPI Debug**
```python
app = FastAPI(debug=True)

# Or in Uvicorn
uvicorn main:app --reload --log-level debug
```

### 15.3 Log File Locations

- **Streamlit:** Console output (no file logging by default)
- **FastAPI:** Console output (configure in code)
- **Python:** Use logging module for file output

**Configure logging to file:**
```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

### 15.4 Known Bugs & Workarounds

| Bug | Workaround | Status |
|-----|-----------|--------|
| SVG icons showing as code | Use emoji icons instead | ✅ Fixed |
| Slow initial load | Increased caching | ✅ Improved |
| CORS errors in cloud | Configure CORS middleware | ⏳ Monitor |

---

## 16. Contributing Guidelines

### 16.1 Code Style & Conventions

**Python Style Guide:** PEP 8

```python
# Good naming
def calculate_total_cycle_time(cycle_time, cooling_time):
    return cycle_time + cooling_time

# Good formatting
model_data = {
    'name': 'ManufactureIQ',
    'version': '2.0.0',
    'status': 'production'
}

# Docstrings required
def load_model():
    """Load trained model from pickle file.
    
    Returns:
        Pipeline: Loaded model pipeline
    """
```

### 16.2 Branch Naming Conventions

```
main                           # Production branch
develop                        # Development branch
feature/add-new-prediction     # Feature branches
bugfix/fix-column-validation   # Bug fix branches
docs/update-readme             # Documentation branches
```

### 16.3 Commit Message Format

```
feat: Add new ROI calculator feature
^--^  ^----^
|     |
|     Description
|
Type

Types: feat, fix, docs, style, refactor, perf, test, chore
```

**Example:**
```
feat: Implement authentication system
fix: Resolve column name mismatch in predictions
docs: Update deployment guide with cloud steps
```

### 16.4 Pull Request Process

1. **Create feature branch** from `develop`
2. **Make changes** with clear commits
3. **Test thoroughly** locally
4. **Write/update tests** if applicable
5. **Update documentation** as needed
6. **Create PR** with detailed description
7. **Request review** from maintainers
8. **Merge** after approval

**PR Template:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update

## Testing
Describe tests performed

## Checklist
- [ ] Code follows PEP 8
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes
```

---

## 17. Future Enhancements

### 17.1 Planned Features

| Feature | Priority | Est. Effort | Status |
|---------|----------|-------------|--------|
| Dark mode support | Medium | 2 hours | ⏳ Planned |
| Advanced ML models (XGBoost) | High | 1 week | ⏳ Planned |
| Database integration (PostgreSQL) | High | 2 weeks | ⏳ Planned |
| User authentication | High | 3 days | ⏳ Planned |
| Data export (PDF/Excel) | Medium | 1 day | ⏳ Planned |
| Real-time monitoring dashboard | Medium | 1 week | ⏳ Planned |
| Mobile app | Low | 2 weeks | ⏳ Future |
| Multi-language support | Low | 1 week | ⏳ Future |

### 17.2 Known Limitations

1. **Single Model Type** - Only Linear Regression (no ensemble methods)
2. **No Temporal Features** - Basic hour/weekend indicators
3. **Limited Training Data** - 1,000 samples (< ideal 5,000+)
4. **No Interactions** - Linear only, no polynomial features
5. **No Real-time Updates** - Static model (not online learning)
6. **Single User** - No multi-user support
7. **No Audit Trail** - No prediction history tracking
8. **No API Rate Limiting** - Vulnerable to abuse

### 17.3 Roadmap Items

**Q4 2025:**
- ✅ v2.0 UI enhancement (DONE)
- ⏳ Streamlit Cloud deployment
- ⏳ Documentation completion

**Q1 2026:**
- ⏳ Authentication system
- ⏳ Database integration
- ⏳ Advanced ML models

**Q2 2026:**
- ⏳ Real-time monitoring
- ⏳ Mobile app launch
- ⏳ API commercialization

---

## 18. Credits and References

### 18.1 Third-Party Libraries Acknowledgments

- **Streamlit** - Amazing web framework for ML apps
- **Plotly** - Beautiful interactive visualizations
- **scikit-learn** - Excellent ML library
- **FastAPI** - Modern, fast API framework
- **pandas** - Data manipulation powerhouse
- **numpy** - Numerical computing foundation

### 18.2 External Resources & Documentation Links

**Official Documentation:**
- Streamlit: https://docs.streamlit.io
- FastAPI: https://fastapi.tiangolo.com
- scikit-learn: https://scikit-learn.org
- Plotly: https://plotly.com/python
- pandas: https://pandas.pydata.org

**Learning Resources:**
- Streamlit Tutorials: https://streamlit.io/docs/tutorial
- Machine Learning Guide: https://scikit-learn.org/stable/modules/linear_model.html
- REST API Best Practices: https://restfulapi.net

**Deployment Guides:**
- Streamlit Cloud: https://share.streamlit.io
- Docker: https://docs.docker.com
- GitHub Pages: https://pages.github.com

### 18.3 Team Members & Contributors

| Role | Name | GitHub | Email |
|------|------|--------|-------|
| Developer | Jay Prakash Kumar | @JayAtria-7 | jay.prakash7.kr@gmail.com |
| Project | ManufactureIQ | - | - |

### 18.4 Acknowledgments

- Machine Learning course for project guidance
- Manufacturing dataset providers
- Open-source community for excellent tools

---

## Appendix A: Quick Reference Commands

### Development Setup
```bash
git clone https://github.com/JayAtria-7/ManufactureIQ.git
cd ManufactureIQ
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Running Applications
```bash
# Streamlit UI
streamlit run app/streamlit_app_v2.py

# FastAPI
cd app && uvicorn main:app --reload

# Jupyter
jupyter notebook capstone_manufacturing_lr.ipynb
```

### Deployment
```bash
# GitHub push
git add . && git commit -m "message" && git push

# Docker
docker build -t manufacture-iq:v2.0 .
docker run -p 8501:8501 manufacture-iq:v2.0

# Streamlit Cloud
# Visit https://share.streamlit.io and deploy
```

---

## Appendix B: Model Prediction Example

### Request Example
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Injection_Temperature": 220,
    "Injection_Pressure": 120,
    "Cycle_Time": 30,
    "Cooling_Time": 12,
    "Material_Viscosity": 250,
    "Ambient_Temperature": 22,
    "Machine_Age": 5,
    "Operator_Experience": 24,
    "Maintenance_Hours": 50
  }'
```

### Response Example
```json
{
  "predicted_parts_per_hour": 47.3,
  "input": {
    "Injection_Temperature": 220,
    "Injection_Pressure": 120,
    "Cycle_Time": 30,
    "Cooling_Time": 12,
    "Material_Viscosity": 250,
    "Ambient_Temperature": 22,
    "Machine_Age": 5,
    "Operator_Experience": 24,
    "Maintenance_Hours": 50
  },
  "derived_features": {
    "Temperature_Pressure_Ratio": 1.833,
    "Total_Cycle_Time": 42
  }
}
```

---

## Appendix C: File Checklist for Deployment

- ✅ `app/streamlit_app_v2.py` - Main Streamlit app
- ✅ `models/model_pipeline.pkl` - Trained model
- ✅ `models/metadata.json` - Model metadata
- ✅ `.streamlit/config.toml` - Streamlit config
- ✅ `requirements_streamlit.txt` - Dependencies
- ✅ `.gitignore` - Git ignore rules
- ✅ `README.md` - Project readme
- ✅ `.github/workflows/` - CI/CD (optional)

---

**Documentation Version:** 2.0.0  
**Last Updated:** October 28, 2025  
**Status:** Complete & Production Ready ✅

For questions or updates, contact: jay.prakash7.kr@gmail.com
