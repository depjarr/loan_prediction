import streamlit as st
import pandas as pd
import joblib 


# Load the model
model = joblib.load("./loan_prediction_model.pkl")

st.title("Loan Approval Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
income = st.number_input("Applicant Income", min_value=0, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, step=1000)
credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", ["1", "0"])

# Encoding input
gender_val = 1 if gender == "Male" else 0
married_val = 1 if married == "Yes" else 0

input_data = pd.DataFrame([{  
    "Gender": gender_val,
    "Married": married_val,
    "ApplicantIncome": income,
    "LoanAmount": loan_amount,
    "Credit_History": credit_history
}])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "Approved" if prediction == 1 else "Rejected"
    st.success(f"Loan Status: {result}")
    