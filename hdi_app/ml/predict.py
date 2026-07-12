import pickle
import numpy as np
from hdi_app.ml.preprocessing import get_hdi_category
import os

class HDIPredictor:
    def __init__(self, model_path, scaler_path):
        self.model_path = model_path
        self.scaler_path = scaler_path
        self.model = None
        self.scaler = None
        self.load_models()
        
    def load_models(self):
        """Load the trained model and scaler from disk."""
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            with open(self.scaler_path, 'rb') as f:
                self.scaler = pickle.load(f)
        else:
            print("Models not found. Please train the pipeline first.")
            
    def predict(self, life_expectancy, mean_years_schooling, expected_years_schooling, gni_per_capita):
        """Make a prediction."""
        if not self.model or not self.scaler:
            raise ValueError("Model or scaler is not loaded.")
            
        features = np.array([[
            life_expectancy,
            mean_years_schooling,
            expected_years_schooling,
            gni_per_capita
        ]])
        
        scaled_features = self.scaler.transform(features)
        
        # Predict
        prediction = self.model.predict(scaled_features)[0]
        
        # Clip to plausible range
        prediction = np.clip(prediction, 0.0, 1.0)
        
        category = get_hdi_category(prediction)
        
        return {
            'score': round(float(prediction), 4),
            'category': category
        }
