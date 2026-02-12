import streamlit as st
from yield_engine import predict_yield
from database import create_table, save_record, fetch_records

st.set_page_config(
    page_title="AgroIntel Crop Disease and Yield Intelligence",
    layout="wide"
)

create_table()

st.title("🌾 AgroIntel – Crop Disease and Yield Intelligence")
st.markdown("AI-powered crop disease detection and yield risk estimation platform.")
st.markdown("---")

# ---------------------------
# IMAGE INPUT SECTION
# ---------------------------
st.markdown("## 📷 Leaf Image Input")

input_mode = st.radio(
    "Choose Image Input Method:",
    ["Use Camera", "Upload Image"]
)

image = None

if input_mode == "Use Camera":
    image = st.camera_input("Capture Leaf Image")
elif input_mode == "Upload Image":
    image = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

if image is not None:
    st.image(image, caption="Selected Leaf Image", use_container_width=True)
    st.success("Image received successfully ✅")

st.markdown("---")

# ---------------------------
# FARM INPUT SECTION
# ---------------------------
st.markdown("## 🌱 Enter Farm Details")

col1, col2 = st.columns(2)

with col1:
    crop = st.selectbox("Select Crop Type", [
        "tomato", "potato", "grapes",
        "apples", "strawberry", "corn"
    ])

with col2:
    land_size = st.number_input("Land Size (Acres)", min_value=0.1, step=0.1)
    temperature = st.number_input("Temperature (°C)", step=1.0)

st.markdown("---")

# ---------------------------
# PREDICTION SECTION
# ---------------------------
if st.button("🚀 Predict Yield & Risk"):

    if image is None:
        st.warning("Please upload or capture a leaf image first.")
    else:

        # TEMPORARY: Dummy ML prediction
        # Replace this with TensorFlow model inference later
        predicted_severity = "moderate"
        predicted_confidence = 82.5

        result = predict_yield(
            crop,
            predicted_severity,
            predicted_confidence,
            land_size,
            temperature
        )

        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Prediction Complete ✅")

            st.markdown("### 🤖 AI Prediction")
            st.metric("Predicted Severity", predicted_severity)
            st.metric("Model Confidence (%)", predicted_confidence)

            colA, colB, colC = st.columns(3)

            colA.metric("Total Possible Yield (tons)", result["total_possible_yield_tons"])
            colB.metric("Estimated Yield (tons)", result["estimated_yield_tons"])
            colC.metric("Yield Loss (tons)", result["yield_loss_tons"])

            st.markdown("### 💰 Economic Impact")
            st.metric("Economic Loss (INR)", f"₹ {result['economic_loss_inr']}")

            st.markdown("### ⚠ Risk Assessment")
            st.metric("Risk Level", result["risk_level"])

            save_record(
                crop,
                predicted_severity,
                predicted_confidence,
                land_size,
                temperature,
                result["total_possible_yield_tons"],
                result["final_reduction_percent"],
                result["yield_loss_tons"],
                result["estimated_yield_tons"],
                result["economic_loss_inr"],
                result["risk_level"]
            )

            st.info("Record saved to database successfully.")

st.markdown("---")

# ---------------------------
# HISTORY SECTION
# ---------------------------
st.subheader("📊 Previous Records")

if st.button("Load Previous Records"):
    records = fetch_records()

    if records:
        st.dataframe(records, use_container_width=True)
    else:
        st.warning("No records found.")