import streamlit as st
import numpy as np
import pandas as pd
from prediction import detection

# Set title and style
st.title('Heart Disease Detection')
# st.markdown('<h2 style="color:blue;">Please fill out the form below to predict heart disease.</h2>', unsafe_allow_html=True)

# Create a form
with st.form(key='heart_disease_form'):
    age = st.number_input('Enter Age of Patient', min_value=0, step=1)

    sex = st.selectbox('Select Gender', ['Male', 'Female'])

    cp = st.selectbox("Chest Pain Type", ['Typical Angina', 'Atypical Angina', 'Non-Anginal', 'Asymptomatic'])

    trestbps = st.number_input('Enter resting blood pressure', min_value=0)

    chol = st.number_input('Enter cholesterol in mg/dl', min_value=0)

    fbs = st.selectbox("Fasting Blood Sugar", ["Normal", "High"])

    restecg = st.selectbox("Resting Electrocardiographic Results",
                           ["Normal", "ST-T wave abnormality", "Left Ventricular hypertrophy"])

    thalach = st.number_input('Enter max heart rate', min_value=0)

    exang = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])

    oldpeak = st.number_input('Enter ST depression', min_value=0.0)

    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])

    ca = st.number_input('Enter number of vessels (0-4)', min_value=0, max_value=4)

    thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversable Defect"])

    # Submit button
    submit_button = st.form_submit_button("Submit")

    # Check if the form is filled out completely
    if submit_button:
        if age == 0 or not sex or not cp or trestbps == 0 or chol == 0 or not fbs or not restecg or thalach == 0 or not exang or oldpeak < 0.0 or not slope or ca < 0 or not thal:
            st.error("Please fill out all fields.")
        else:
            with st.spinner("Processing..."):
                # Convert categorical data to numerical values
                sex = 1 if sex == 'Male' else 0
                cp = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal': 2, 'Asymptomatic': 3}[cp]
                fbs = 1 if fbs == "High" else 0
                restecg = {'Normal': 0, 'ST-T wave abnormality': 1, 'Left Ventricular hypertrophy': 2}[restecg]
                exang = 1 if exang == 'Yes' else 0
                slope = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}[slope]
                thal = {'Normal': 0, 'Fixed Defect': 1, 'Reversable Defect': 2}[thal]

                # Call prediction function
                pred = detection(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

                if pred == 1:
                    st.success("Prediction: Heart Disease Detected!")
                else:
                    st.success("Prediction: No Heart Disease Detected.")
