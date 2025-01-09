import pickle
import numpy as np
import warnings

# Suppress the specific warning
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Load the pre-trained model
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Detection function for heart disease prediction
def detection(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Prepare the input data as a tuple and reshape it for prediction
    input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    inputs = np.array(input_data).reshape(1, -1)

    # Make the prediction
    prediction = loaded_model.predict(inputs)[0]
    return prediction
