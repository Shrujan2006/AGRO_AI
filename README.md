🌾 AgroIntel – Offline Leaf Disease Detection & Yield Prediction
🚀 Project Overview
AgroIntel is an AI-powered agricultural support system designed to help farmers detect crop diseases from leaf images and estimate potential yield loss — even in offline environments.
The goal of this project is to provide:
🌿 Instant leaf disease detection using deep learning
📉 Estimated yield impact calculation
💰 Economic loss prediction
📴 Offline functionality for rural areas with limited internet access
🎯 Problem Statement
Farmers often struggle with:
Late disease detection
Lack of expert consultation access
Uncertainty about yield loss
No data-driven financial estimation
AgroIntel solves this by combining Computer Vision + Predictive Logic + Local Storage in a lightweight system.
🧠 System Architecture
Current MVP Structure
AgroIntel/
│
├── app.py              # Streamlit UI
├── yield_engine.py     # Yield & economic loss logic
├── database.py         # SQLite storage
├── model.h5            # Trained leaf disease model
├── agroai.db           # Local database
└── README.md
🌿 Leaf Disease Detection Module
🔍 How It Works
User uploads a leaf image
Image is preprocessed
Trained TensorFlow/Keras model (.h5) predicts:
Crop Type
Disease Type
Confidence Score
Severity is derived from confidence
Yield loss is estimated
🧮 Yield Prediction Logic
The system calculates:
Base yield per acre (crop specific)
Disease severity multiplier
Adjusted yield
Estimated financial loss
Formula Used
Loss = Base_Yield × Severity_Factor × Land_Size
Economic_Loss = Loss × Market_Price
💾 Database Design (SQLite)
The system stores farmer records locally.
Table: records
Field	Type
id	INTEGER (Primary Key)
farmer_name	TEXT
crop	TEXT
disease	TEXT
confidence	REAL
severity	TEXT
land_size	REAL
temperature	REAL
rainfall	REAL
predicted_yield	REAL
economic_loss	REAL
timestamp	DATETIME
📴 Offline Capability
AgroIntel is designed to run:
On a local machine
Without internet
Using a pre-trained .h5 model
With SQLite for storage
Future version:
Convert into Android app (TensorFlow Lite)
Edge device deployment
🛠️ Tech Stack
Python 3.10–3.12 (TensorFlow compatible)
TensorFlow / Keras
Streamlit
SQLite3
NumPy
Pillow (Image Processing)
⚙️ Installation Guide (Mac/Linux)
1️⃣ Create Virtual Environment (Important for TensorFlow)
python3.12 -m venv agroenv
source agroenv/bin/activate
2️⃣ Install Dependencies
pip install tensorflow streamlit numpy pillow
3️⃣ Run Application
streamlit run app.py
👥 Team Work Division (Hackathon Mode)
Role	Responsibility
ML Engineer	Model training & tuning
Backend Dev	yield_engine.py logic
Database Dev	SQLite integration
Frontend Dev	Streamlit UI
Integration Lead	Testing & deployment
🔮 Future Improvements
Convert model to TensorFlow Lite
Android offline mobile app
Real-time weather API integration
Cloud dashboard for agricultural analytics
Multi-language farmer interface
🏆 Hackathon Vision
AgroIntel aims to become a scalable, AI-driven agricultural assistant that:
Empowers farmers
Reduces crop loss
Improves rural profitability
Works even without internet
📌 Project Status
✅ Leaf Disease Detection – Model Ready
✅ Yield Calculation Engine – Implemented
✅ Local Database – Working
🔄 Mobile Deployment – Planned
