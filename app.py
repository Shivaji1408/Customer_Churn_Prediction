import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model, scaler, and column names
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Create empty dictionary for inputs
input_dict = {}

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("📊 Customer Churn Prediction App")
st.write("Provide customer details to predict whether they will churn.")

# Identify one-hot encoded categorical columns
categorical_options = {
    'gender': ['Female', 'Male'],
    'Partner': ['No', 'Yes'],
    'Dependents': ['No', 'Yes'],
    'PhoneService': ['No', 'Yes'],
    'MultipleLines': ['No phone service', 'No', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No internet service', 'No', 'Yes'],
    'OnlineBackup': ['No internet service', 'No', 'Yes'],
    'DeviceProtection': ['No internet service', 'No', 'Yes'],
    'TechSupport': ['No internet service', 'No', 'Yes'],
    'StreamingTV': ['No internet service', 'No', 'Yes'],
    'StreamingMovies': ['No internet service', 'No', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['No', 'Yes'],
    'PaymentMethod': ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check']
}

# Handle categorical fields
for col, options in categorical_options.items():
    selected = st.selectbox(f"{col}", options)
    for opt in options:
        key = f"{col}_{opt}"
        input_dict[key] = 1 if selected == opt else 0

# Handle numeric fields
input_dict['SeniorCitizen'] = st.selectbox("SeniorCitizen", [0, 1])
input_dict['tenure'] = st.number_input("Tenure (in months)", min_value=0, max_value=72)
input_dict['MonthlyCharges'] = st.number_input("Monthly Charges", min_value=0.0)
input_dict['TotalCharges'] = st.number_input("Total Charges", min_value=0.0)

# Convert to DataFrame in same order as training
input_df = pd.DataFrame([input_dict])
# Ensure all expected columns are present
for col in columns:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[columns]  # Ensure column order

# Scale numeric features
scaled_input = scaler.transform(input_df)

# Predict on button click
if st.button("Predict Churn"):
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    if prediction == 1:
        st.error(f"❌ Customer is likely to churn.")
    else:
        st.success(f"✅ Customer is likely to stay.")
