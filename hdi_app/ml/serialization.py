import pickle
import json
import os
from datetime import datetime

def save_model(model, name, metrics, feature_columns, filepath):
    """Serialize the best model and metadata."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
        
    metadata = {
        'algorithm_name': name,
        'metrics': metrics,
        'feature_columns': feature_columns,
        'training_date': datetime.utcnow().isoformat(),
        'version': '1.0'
    }
    
    metadata_path = filepath.replace('.pkl', '_metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)
        
    return metadata

def save_preprocessors(scaler, encoder, filepath_prefix):
    """Serialize preprocessors."""
    os.makedirs(os.path.dirname(filepath_prefix), exist_ok=True)
    
    with open(f"{filepath_prefix}_scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
        
    if encoder:
        with open(f"{filepath_prefix}_encoder.pkl", "wb") as f:
            pickle.dump(encoder, f)
