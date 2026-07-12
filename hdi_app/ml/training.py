from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
try:
    from xgboost import XGBRegressor
    XGB_AVAILABLE = True
except ImportError:
    XGB_AVAILABLE = False

from hdi_app.ml.evaluation import evaluate_model

def train_multiple_models(X_train, y_train):
    """Train multiple regression models."""
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    if XGB_AVAILABLE:
        models['XGBoost'] = XGBRegressor(n_estimators=100, random_state=42)
        
    trained_models = {}
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model
        
    return trained_models

def select_best_model(trained_models, X_test, y_test):
    """Select the best model based on R2 Score."""
    best_model = None
    best_name = None
    best_metrics = {'r2': -float('inf')}
    
    all_metrics = {}
    
    for name, model in trained_models.items():
        metrics = evaluate_model(model, X_test, y_test)
        all_metrics[name] = metrics
        
        if metrics['r2'] > best_metrics['r2']:
            best_metrics = metrics
            best_model = model
            best_name = name
            
    print(f"\nBest Model: {best_name} (R2: {best_metrics['r2']:.4f})")
    return best_model, best_name, best_metrics, all_metrics

