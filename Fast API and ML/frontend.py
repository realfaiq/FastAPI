import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Loan Eligibility Preidictor")

st.markdown("Please Enter the below details")

age = st.number_input("Age", min_value=1, max_value=120)
income = st.number_input("Income", min_value=1)
loan_amount = st.number_input("Loan Amount", min_value=1)
credit_score = st.number_input("Credit Score", min_value=1) 
years_employed = st.number_input("Years Employed", min_value=1)
has_defaulted_before = st.selectbox("has_defaulted_before if yes select 1 otherwise 0", options=[0, 1])
    
if st.button("Predict Eligibility"):
    input_data = {
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "credit_score": credit_score,
        "years_employed": years_employed,
        "has_defaulted_before": has_defaulted_before
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running on port 8000.")