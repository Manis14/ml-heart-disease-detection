# Heart Disease Detection Web Application
Link: https://ml-heart-disease-detection-jy6qxybe2r86q3j2njlrpb.streamlit.app/ 
## Project Description

This project is a machine learning-based web application for detecting heart disease using various health-related features such as age, blood pressure, cholesterol, exercise-induced angina, and more. The model is built using **Logistic Regression**, and the web interface is built using **Streamlit**.

The application takes user input through a simple form and predicts whether the user is at risk of heart disease or not. The model provides an output based on the input features, with a binary classification of whether heart disease is detected or not.

## Features

- Interactive web interface using Streamlit.
- User-friendly form to input data related to heart health.
- Predicts whether the user has heart disease or not.
- Model metrics provided for performance evaluation.

## Model Information

- **Model Type**: Logistic Regression
- **Accuracy**: 0.8049
- **Confusion Matrix**: [[72 28] [12 93]]
  

- **F1 Score**: 0.8230
- **Recall**: 0.8857
- **Precision**: 0.7686

These metrics show that the model is able to detect heart disease with high accuracy and performs well in terms of recall, ensuring that most patients with heart disease are correctly identified.

## Requirements

- **streamlit**: For building the web application.
- **numpy**: For numerical operations.
- **pandas**: For handling data.
- **scikit-learn**: For the machine learning model and evaluation metrics.

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```
## Example of the Input Form
- Age of patient
- Gender
- Chest pain type
- Resting blood pressure
- Cholesterol level
- Fasting blood sugar
- Electrocardiographic results
- Maximum heart rate
- Exercise-induced angina
- ST depression
- Slope of the peak exercise ST segment
- Number of vessels (0-4)
- Thalassemia type


## Look of Frontend
![image](https://github.com/user-attachments/assets/936ed4b0-6340-4f37-9a84-d049b73dd3ef)

