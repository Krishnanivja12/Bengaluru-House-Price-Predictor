import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import gdown

import streamlit as st
import pandas as pd
import pickle

# -------------------- Page Config --------------------
st.set_page_config(page_title="🏠 Bengaluru Price Predictor", layout="centered")
st.title("🏡 Bengaluru House Price Predictor")
st.markdown("### Enter the details below to estimate the price of a property in Bengaluru.")

# -------------------- Load Model --------------------
try:
    with open("random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error("❌ Model file not found or corrupted.")
    st.stop()

# -------------------- Valid Input Options --------------------
location_options = [
    'Whitefield', 'Electronic City', 'Rajaji Nagar',
    'Marathahalli', 'HSR Layout', 'Indira Nagar'
    # Add more if needed
]

# -------------------- User Input UI --------------------
st.subheader("📋 Property Details")
location = st.selectbox("📍 Location", sorted(location_options))
sqft = st.number_input("📐 Total Square Feet", min_value=300, max_value=10000, step=50)
bath = st.slider("🛁 Bathrooms", min_value=1, max_value=5, value=2)
bhk = st.slider("🛏️ BHK (Bedrooms)", min_value=1, max_value=6, value=2)

# -------------------- Predict Button Logic --------------------
if st.button("🔍 Predict Price"):
    try:
        # Prepare input DataFrame
        input_data = pd.DataFrame([[location, sqft, bath, bhk]],
                                  columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Predict
        prediction = model.predict(input_data)[0]
        prediction = max(0, prediction)

        st.success(f"💰 Estimated Price: ₹ {round(prediction, 2)} Lakhs")

    except Exception as e:
        st.error(f"❌ Something went wrong during prediction:\n`{e}`")
