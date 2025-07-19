# 🏡 Bengaluru House Price Prediction

This project predicts housing prices in Bengaluru based on features like square footage, number of bedrooms, bathrooms, and location. A machine learning model is trained and deployed using Streamlit for real-time predictions.

## 🔧 Tech Stack

- Python  
- Scikit-learn  
- Pandas, NumPy  
- Streamlit  
- Pickle  
- gdown  

## 📁 Project Structure

📁 bangalore-house-price<br>
├── app.py # Streamlit web app<br>
├── random_forest_model.pkl # Trained ML model<br>
├── requirements.txt # Dependencies<br>
└── README.md

## 📊 Features

- Predicts house prices based on:
  - Location
  - Total square feet
  - Number of bathrooms
  - Number of bedrooms (BHK)
- Simple and clean Streamlit interface
- Model loaded directly from Google Drive using `gdown`

## 📈 Model Info

- Model: Random Forest Regressor  
- Dataset: Real estate listings from Bengaluru  
- Preprocessing: Label encoding, outlier removal, feature selection

## ✍️ Author

**Krishna Nivja**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/krishnanivja/)
