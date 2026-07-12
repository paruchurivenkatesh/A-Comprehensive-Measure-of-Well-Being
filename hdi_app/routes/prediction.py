from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from hdi_app.ml.predict import HDIPredictor
from hdi_app.models.database_models import PredictionHistory
from hdi_app import db
from config import Config
import os

prediction_bp = Blueprint('prediction', __name__)

def get_predictor():
    model_path = os.path.join(Config.MODELS_DIR, 'best_model.pkl')
    scaler_path = os.path.join(Config.MODELS_DIR, 'preprocessing_scaler.pkl')
    try:
        return HDIPredictor(model_path, scaler_path)
    except Exception as e:
        print(f"Error loading predictor: {e}")
        return None

@prediction_bp.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        try:
            country = request.form.get('country')
            life_expectancy = float(request.form.get('life_expectancy'))
            mean_years_schooling = float(request.form.get('mean_years_schooling'))
            expected_years_schooling = float(request.form.get('expected_years_schooling'))
            gni_per_capita = float(request.form.get('gni_per_capita'))
            
            predictor = get_predictor()
            if not predictor:
                flash('Model is currently unavailable. Please contact an administrator.', 'danger')
                return render_template('predict.html')
                
            result = predictor.predict(
                life_expectancy, mean_years_schooling, expected_years_schooling, gni_per_capita
            )
            
            # Save to history
            history = PredictionHistory(
                user_id=current_user.id,
                country=country,
                life_expectancy=life_expectancy,
                mean_years_schooling=mean_years_schooling,
                expected_years_schooling=expected_years_schooling,
                gni_per_capita=gni_per_capita,
                predicted_hdi=result['score'],
                predicted_category=result['category']
            )
            db.session.add(history)
            db.session.commit()
            
            return render_template('predict.html', result=result, form_data=request.form)
            
        except ValueError:
            flash('Invalid input. Please enter numerical values.', 'danger')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
            
    return render_template('predict.html')

@prediction_bp.route('/api/predict', methods=['POST'])
def api_predict():
    """REST API endpoint for prediction"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
        
    try:
        predictor = get_predictor()
        if not predictor:
            return jsonify({'error': 'Model unavailable'}), 503
            
        result = predictor.predict(
            float(data['life_expectancy']),
            float(data['mean_years_schooling']),
            float(data['expected_years_schooling']),
            float(data['gni_per_capita'])
        )
        
        return jsonify({
            'status': 'success',
            'score': result['score'],
            'category': result['category']
        }), 200
        
    except KeyError as e:
        return jsonify({'error': f'Missing parameter {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
