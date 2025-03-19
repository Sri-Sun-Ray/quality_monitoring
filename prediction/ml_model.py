import joblib
import numpy as np

# Load the trained model
model = joblib.load("water_quality_model.pkl")

# Function to make predictions
def predict_water_quality(features):
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]  # 0: Unsafe, 1: Safe
    return prediction




'''import joblib
import numpy as np

# Load the saved model
model = joblib.load("svm_water_quality.pkl")

def predict_water_quality(data):
    """
    Function to predict water quality based on input features.
    :param data: List of 9 numerical values representing water parameters.
    :return: 0 (Unsafe) or 1 (Safe)
    """
    data = np.array(data).reshape(1, -1)  # Reshape for prediction
    prediction = model.predict(data)
    return int(prediction[0])  # Convert NumPy int to Python int'''