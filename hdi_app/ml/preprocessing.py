import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
import os

def load_data(filepath):
    """Load dataset from CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    return pd.read_csv(filepath)

def clean_data(df):
    """Handle missing values and duplicates."""
    df_cleaned = df.copy()
    
    # Remove duplicates
    df_cleaned = df_cleaned.drop_duplicates()
    
    # Impute missing values with column means for numerical columns
    numerical_cols = ['Life Expectancy', 'Expected Years of Schooling', 'Mean Years of Schooling', 'Gross National Income Per Capita']
    for col in numerical_cols:
        if col in df_cleaned.columns:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mean())
            
    # For target columns, drop rows with missing targets
    if 'HDI Score' in df_cleaned.columns:
        df_cleaned = df_cleaned.dropna(subset=['HDI Score'])
        
    return df_cleaned

def engineer_features(df):
    """Select independent variables (X) and target variable (y)."""
    # Features mentioned in requirements
    features = [
        'Life Expectancy',
        'Mean Years of Schooling',
        'Expected Years of Schooling',
        'Gross National Income Per Capita'
    ]
    
    X = df[features]
    y = df['HDI Score']
    
    return X, y

def preprocess_and_split(X, y, test_size=0.25, random_state=42):
    """Scale features and split dataset."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

def get_hdi_category(score):
    """Categorize HDI Score according to UNDP ranges."""
    if score >= 0.800:
        return 'Very High'
    elif score >= 0.700:
        return 'High'
    elif score >= 0.550:
        return 'Medium'
    else:
        return 'Low'
