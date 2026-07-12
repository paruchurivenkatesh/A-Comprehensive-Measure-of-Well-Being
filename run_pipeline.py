import os
from hdi_app.ml.data_generator import generate_synthetic_dataset
from hdi_app.ml.preprocessing import load_data, clean_data, engineer_features, preprocess_and_split
from hdi_app.ml.training import train_multiple_models, select_best_model
from hdi_app.ml.visualization import generate_eda_plots
from hdi_app.ml.serialization import save_model, save_preprocessors
from config import Config
from hdi_app import create_app, db
from hdi_app.models.database_models import ModelMetadata
from hdi_app.database.init_db import initialize_database

def run_pipeline():
    print("Starting ML Pipeline...")
    
    # Paths
    raw_data_path = os.path.join(Config.DATA_DIR, 'raw', 'hdi_data.csv')
    processed_data_path = os.path.join(Config.DATA_DIR, 'processed', 'hdi_data_clean.csv')
    best_model_path = os.path.join(Config.MODELS_DIR, 'best_model.pkl')
    preprocessors_prefix = os.path.join(Config.MODELS_DIR, 'preprocessing')
    eda_output_dir = os.path.join(Config.BASE_DIR, 'hdi_app', 'static', 'images', 'eda')
    
    # 1. Ensure data exists (generate synthetic if not)
    if not os.path.exists(raw_data_path):
        generate_synthetic_dataset(raw_data_path)
        
    # 2. Load Data
    print("Loading data...")
    df = load_data(raw_data_path)
    
    # 3. Clean Data
    print("Cleaning data...")
    df_clean = clean_data(df)
    df_clean.to_csv(processed_data_path, index=False)
    
    # 4. Generate EDA
    print("Generating EDA plots...")
    generate_eda_plots(df_clean, eda_output_dir)
    
    # 5. Feature Engineering
    print("Engineering features...")
    X, y = engineer_features(df_clean)
    feature_columns = list(X.columns)
    
    # 6. Preprocess and split
    print("Preprocessing and splitting data...")
    X_train, X_test, y_train, y_test, scaler = preprocess_and_split(X, y)
    save_preprocessors(scaler, None, preprocessors_prefix)
    
    # 7. Train models
    print("Training models...")
    trained_models = train_multiple_models(X_train, y_train)
    
    # 8. Evaluate and select best
    print("Selecting best model...")
    best_model, best_name, best_metrics, _ = select_best_model(trained_models, X_test, y_test)
    
    # 9. Save best model
    print(f"Saving best model ({best_name}) to {best_model_path}")
    save_model(best_model, best_name, best_metrics, feature_columns, best_model_path)
    
    # 10. Update database with new model metadata
    app = create_app()
    with app.app_context():
        # Ensure database is initialized
        initialize_database()
        
        # Deactivate old models
        ModelMetadata.query.update({ModelMetadata.is_active: False})
        
        # Insert new metadata
        new_meta = ModelMetadata(
            algorithm_name=best_name,
            r2_score=best_metrics['r2'],
            mae=best_metrics['mae'],
            mse=best_metrics['mse'],
            rmse=best_metrics['rmse'],
            is_active=True
        )
        db.session.add(new_meta)
        db.session.commit()
        print("Database updated with model metadata.")
        
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
