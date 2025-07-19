import streamlit as st
import pandas as pd
import joblib

# Load the trained Ridge pipeline
ridge_pipeline = joblib.load("ridge_salary_model.pkl")

st.title("Salary Prediction App 💼")

st.write("Enter the details below to predict the salary:")

# Create input widgets
education = st.selectbox("Education", ["High School", "Bachelor's", "Master's", "PhD"])
experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
location = st.selectbox("Location", ["New York", "San Francisco", "Los Angeles", "Chicago", "Remote"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "Product Manager", "Designer", "Other"])
age = st.number_input("Age", min_value=18, max_value=70, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# When the button is clicked, predict salary
if st.button("Predict Salary"):
    # Create DataFrame from inputs
    input_data = pd.DataFrame({
        'Education': [education],
        'Experience': [experience],
        'Location': [location],
        'Job_Title': [job_title],
        'Age': [age],
        'Gender': [gender]
    })

    # Predict salary
    predicted_salary = ridge_pipeline.predict(input_data)[0]

    st.success(f"Estimated Salary: ${predicted_salary:,.2f}")
