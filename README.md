🌾 AgroIntel
Offline Leaf Disease Detection & Yield Prediction System
📌 Overview
AgroIntel is an AI-powered agricultural support system designed to help farmers:
🌿 Detect crop diseases from leaf images
📉 Estimate yield reduction
💰 Calculate potential economic loss
📴 Work completely offline
The system combines Computer Vision, Predictive Logic, and Local Database Storage to provide practical decision support for farmers in rural areas.
🎯 Problem Statement
Farmers often face:
Late disease detection
No access to agricultural experts
Uncertainty about yield impact
No financial loss estimation
AgroIntel provides instant AI-based diagnosis and yield analysis using only a leaf image.
🧠 How the System Works
Farmer uploads a leaf image.
The trained deep learning model (model.h5) predicts:
Crop type
Disease type
Confidence score
Disease severity is calculated.
Yield loss is estimated using crop-specific base yield.
Economic loss is calculated.
Data is stored locally in SQLite database.
🏗️ Project Structure
AgroIntel/
│
├── app.py              # Streamlit User Interface
├── yield_engine.py     # Yield & loss calculation logic
├── database.py         # SQLite database functions
├── model.h5            # Trained leaf disease detection model
├── agroai.db           # Local database file
└── README.md
🧮 Yield Calculation Logic
The system estimates yield loss using:
Base yield per acre (crop-specific)
Disease severity factor
Land size
Market price
Core Formula
Estimated Loss = Base_Yield × Severity_Factor × Land_Size
Economic Loss = Estimated_Loss × Market_Price
