
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
os.system("pip install gdown")
import gdown

# ----------- Download Model from Google Drive ------------
file_id = "1lg5iXEX3www0hJw_wuCmbCikPE_PGi6N"
url = f"https://drive.google.com/uc?id={file_id}"
output = "random_forest_model.pkl"

if not os.path.exists(output):
    with st.spinner("Downloading ML model..."):
        gdown.download(url, output, quiet=False)

# ----------- Load the Model ----------------
with open(output, "rb") as file:
    model = pickle.load(file)

# Define valid location options (only those used during training)
location_options = [
    'Whitefield', 'Electronic City', 'Rajaji Nagar',
    'Marathahalli', 'HSR Layout', 'Indira Nagar'
    # ➕ Add all valid locations here used in training
]

# Streamlit UI
st.set_page_config(page_title="🏠 Bengaluru Price Predictor")
st.title("🏡 Bengaluru House Price Predictor")
st.markdown("Fill in the details below to estimate house price (in Lakhs).")

# Input fields
location = st.selectbox("📍 Location", sorted(location_options))
sqft = st.number_input("📐 Total Square Feet", min_value=300, max_value=10000, step=50)
bath = st.slider("🛁 Bathrooms", 1, 5, 2)
bhk = st.slider("🛏️ BHK (Bedrooms)", 1, 6, 2)

# Predict button
if st.button("🔍 Predict Price"):
    try:
        # Create a DataFrame with only 4 features
        input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                                columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Predict using pipeline model
        predicted_price = model.predict(input_df)[0]
        predicted_price = max(0, predicted_price)  # Ensure price is non-negative

        st.success(f"💰 Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
