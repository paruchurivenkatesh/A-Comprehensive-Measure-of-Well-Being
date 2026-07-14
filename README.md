# 🌍 A Comprehensive Measure of Well-Being (HDI Prediction System)

## 📌 Project Overview
The Human Development Index (HDI) Prediction System is an intelligent, Machine Learning-backed web application developed to analyze and forecast the social and economic development tiers of global nations. The system assists researchers, policy analysts, and international organizations in making faster, data-driven developmental assessments by evaluating vital country-level indicators. The application integrates advanced predictive modeling techniques and exposes them through a responsive, glassmorphism-themed Flask web interface for real-time inference.

## 🎯 Problem Statement
Traditional methods of compiling and assessing international development indices are heavily reliant on retrospective, lag-heavy manual data collection, making proactive policy evaluations slow and prone to delayed intervention. This project addresses the challenge by automating socio-economic tier assessments using optimized machine learning techniques, enabling financial and social institutions to improve efficiency and reduce global forecasting risks.

## ER Diagram

<img width="1408" height="711" alt="Gemini_Generated_Image_(entity relation ship)" src="https://github.com/user-attachments/assets/5556fc61-6e76-4000-b068-af004bcccacf" />



## 🚀 Key Features

Experience a complete AI-powered Human Development Index (HDI) analysis platform designed for researchers, students, and policy analysts.

- 🔐 **Secure User Authentication**: User registration and login system with session management using Flask-Login.
- 🌍 **HDI Prediction Engine**: Predicts a country's Human Development Index score and development category using a trained Machine Learning model.
- 📈 **Interactive Dashboard**: Displays prediction statistics, historical records, and analytical insights for users.
- 📝 **Prediction History Management**: Automatically stores every prediction in a SQLite database for future reference.
- 📄 **Report Generation**: View and analyze detailed prediction reports directly within the application.
- ⚡ **Real-Time ML Inference**: Loads the trained model and preprocessing scaler to generate predictions instantly.
- 🛡️ **Input Validation & Error Handling**: Validates user inputs and provides informative feedback for invalid data.
- 🎨 **Responsive Modern Interface**: Clean, mobile-friendly UI built with HTML5, CSS3, Bootstrap, and Jinja2 templates.
- 🏗️ **Modular Flask Architecture**: Organized using Blueprints for authentication, prediction, dashboard, reports, and home modules.

---

## 🏗️ System Architecture

The application follows a modular, multi-layer architecture to ensure scalability and maintainability.

### **Presentation Layer**
- Responsive HTML5 Templates
- Bootstrap-based User Interface
- Jinja2 Template Rendering
- Dashboard & Report Pages

### **Application Layer**
- Flask Application Factory Pattern
- Blueprint-based Route Management
- User Authentication & Session Handling
- Form Validation and Request Processing

### **Machine Learning Layer**
- Data Preprocessing & Feature Scaling
- Trained Scikit-Learn Prediction Model
- HDI Score Prediction
- Development Category Classification

### **Database Layer**
- SQLite Database
- SQLAlchemy ORM
- User Management
- Prediction History Storage

### **Utilities**
- Logging Utilities
- Database Initialization
- Configuration Management
- Model Serialization

---

## 📊 Dataset Information

The prediction model evaluates a country's Human Development Index using four major socio-economic indicators.

| Feature Dimension | Target Metric Description | Valid Ingestion Bounds | Target Data Type |
| :--- | :--- | :--- | :--- |
| **Country Name** | Name of the nation selected for regional parsing | Dropdown Menu Selection | string |
| **Life Expectancy(Years)** | Life expectancy rate tracking healthcare longevity | e.g., 82.4 Years| float |
| **Mean Years of Schooling** | Mean years of schooling completed by residents | e.g., 12.6 Years | float |
| **Expected Years of Schooling** | Expected years of schooling completed by residents | e.g., 18.1 Years | float |
| **GNI per Capita($)** | Gross National Income per capita (purchasing power) | e.g., $66494 | float |

### **Prediction Output**

The Machine Learning model predicts:

- 📈 Human Development Index (HDI) Score
- 🌍 Development Category (Low, Medium, High, or Very High Human Development)

---

## ⚙️ Tech Stack

| Layer | Component | Description |
| :--- | :--- | :--- |
| **Frontend** | 🌐 HTML5, CSS3, Bootstrap & Jinja2 | Responsive web interface with dynamic templates, dashboard pages, and user-friendly design |
| **Backend** | 🐍 Python & Flask | Modular Flask application using Blueprints, route handling, authentication, and business logic |
| **Authentication** | 🔐 Flask-Login | Secure user registration, login, session management, and access control |
| **Database** | 🗄️ SQLite & SQLAlchemy | Relational database management for users, prediction records, and historical data storage |
| **Machine Learning** | 🤖 Scikit-Learn | Trained regression/classification model for Human Development Index (HDI) prediction |
| **Data Processing** | 📊 Pandas & NumPy | Data cleaning, feature preparation, numerical computations, and preprocessing operations |
| **Model Storage** | 📁 Pickle (.pkl) | Serialized machine learning model and preprocessing scaler for real-time inference |
| **Visualization** | 📈 Matplotlib | Generation of charts, analytical insights, and prediction-related visual reports |
| **Template Engine** | ⚡ Jinja2 | Dynamic rendering of prediction results, dashboards, and report pages |
| **Testing & Development** | 🧪 PyTest & Virtual Environment | Application testing, dependency management, and development workflow support |

## 🗂️ Project Structure
```text
A-Comprehensive-Measure-of-Well-Being/
├── app.py                     # Central Flask backend engine routing script
├── config.py                  # Environment configurations (Dev/Prod)
├── run_pipeline.py            # ML pipeline, model training, and evaluation
├── requirements.txt           # Production environment core dependencies
├── README.md                  # Project documentation
├── dataset/
│   ├── raw/                   # Raw historical master datasets
│   └── processed/             # Cleaned and processed datasets
├── models/
│   └── best_model.pkl         # Pre-trained serialized champion model binary (Generated)
├── hdi_app/                   # Main Application Package
│   ├── __init__.py            # Application factory & extensions
│   ├── database/              # SQLite database storage & init scripts
│   ├── ml/                    # Machine learning logic (preprocessing, training, etc.)
│   ├── models/                # SQLAlchemy database models
│   ├── routes/                # Flask blueprint route definitions (auth, dashboard, etc.)
│   ├── utils/                 # Helper functions & logging
│   ├── static/                
│   │   ├── css/               # Glassmorphism frontend UI layout rules
│   │   ├── js/                # Client-side validation scripts
│   │   └── images/            # Generated EDA plots and assets
│   └── templates/             
│       ├── base.html          # Base HTML layout template
│       ├── index.html         # System introductory overview page
│       ├── predict.html       # Data input metric form
│       ├── dashboard.html     # Categorized results rendering panel
│       ├── history.html       # Prediction history viewer
│       ├── report.html        # Downloadable/printable report layout
│       └── auth/              # Login & Register templates
├── logs/                      # Application runtime logs
└── tests/                     # Unit and Integration Tests
```

## 💻 Installation & Usage

**Initialize the Application Environment**
```bash
# Clone the workspace repository (If applicable)
git clone https://github.com/YOUR_GITHUB_USERNAME/A-Comprehensive-Measure-of-Well-Being.git
cd "A Comprehensive Measure of Well-Being"

# Initialize and lock environment packages
python -m venv venv

# Activate Virtual Environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
# source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the ML Pipeline to generate models and synthetic dataset
python run_pipeline.py

# Start up the local development engine
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000` to interact with the application forms. Log in using the default admin account created during setup (Email: `admin@hdi.org`, Password: `admin123`).

## 💼 Business & Global Use Cases
- **Fast-Track Development Appraisals**: Low-risk regional metric tracking can be completed instantly, minimizing hours spent on traditional census report data pipelines.
- **Risk Identification & Mitigation**: Analysts can pinpoint exact vectors where a country is falling behind (e.g., matching lagging schooling years against dropping health vectors) to re-route local aid allocations.
- **Bulk Policy Simulation**: Simulates micro-development parameter shifts across global subsets to assist strategic planners in evaluating future budget trajectories.

## 🎓 Learning Outcomes
Through this engineering sprint, the following technical competencies were mastered:
- ✔️ End-to-End Predictive Machine Learning Model Development.
- ✔️ Data Visualization & Exploration Analysis workflows.
- ✔️ Object Serialization and Pipeline Preservation using Pickle wrappers.
- ✔️ Robust Flask Full-Stack Web Architecture Routing.
- ✔️ Interface Design utilizing advanced CSS variable configurations.

## 👨‍💻 Author
- 👑 **Paruchuri Venkatesh**
- 👑 **Rokkam Guna Sekhar**

## 📝 Conclusion

The **Human Development Index (HDI) Prediction System** showcases how Artificial Intelligence and Machine Learning can be used to analyze and predict a country's development based on key socio-economic indicators. By combining a trained Machine Learning model with a user-friendly Flask web application, the system provides quick, reliable, and data-driven predictions.

With features such as secure user authentication, prediction history, an interactive dashboard, and real-time HDI prediction, the project demonstrates the complete workflow of building and deploying a Machine Learning application. Overall, it serves as a practical solution for students, researchers, and policy analysts while providing a strong foundation for future enhancements and real-world applications.
