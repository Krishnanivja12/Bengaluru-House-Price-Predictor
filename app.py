import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import gdown

# -------------------- Page Configuration --------------------
st.set_page_config(page_title="🏠 Bengaluru Price Predictor")
st.title("🏡 Bengaluru House Price Predictor")
st.markdown("Estimate house price based on size, BHK, bathrooms and location (in Lakhs ₹)")

# -------------------- Model Download Setup --------------------
file_id = "1lg5iXEX3www0hJw_wuCmbCikPE_PGi6N"
url = f"https://drive.google.com/uc?id={file_id}"
model_filename = "random_forest_model.pkl"

# Download model only if not already downloaded
if not os.path.exists(model_filename):
    with st.spinner("📥 Downloading Machine Learning model..."):
        gdown.download(url, model_filename, quiet=False)

# -------------------- Model Load with Error Handling --------------------
model = None
try:
    with open(model_filename, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error("⚠️ Failed to load the ML model. Please check if the file is a valid pickle file.")
    st.stop()

# -------------------- Valid Input Options --------------------
location_options = [
    'Whitefield', 'Electronic City', 'Rajaji Nagar',
    'Marathahalli', 'HSR Layout', 'Indira Nagar'
    # Add more locations as per your training data
]

# -------------------- User Input UI --------------------
location = st.selectbox("📍 Location", sorted(location_options))
sqft = st.number_input("📐 Total Square Feet", min_value=300, max_value=10000, step=50)
bath = st.slider("🛁 Bathrooms", 1, 5, 2)
bhk = st.slider("🛏️ BHK (Bedrooms)", 1, 6, 2)

# -------------------- Predict Button Logic --------------------
if st.button("🔍 Predict Price"):
    try:
        # Create DataFrame with correct columns
        input_data = pd.DataFrame([[location, sqft, bath, bhk]], 
                                  columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Prediction
        prediction = model.predict(input_data)[0]
        prediction = max(0, prediction)

        st.success(f"💰 Estimated Price: ₹ {round(prediction, 2)} Lakhs")

    except Exception as e:
        st.error(f"❌ Something went wrong during prediction: {e}")
