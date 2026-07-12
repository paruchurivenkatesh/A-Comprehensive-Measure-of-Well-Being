from flask import Blueprint, render_template
from flask_login import login_required, current_user
from hdi_app.models.database_models import PredictionHistory, ModelMetadata
from hdi_app import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def index():
    # User specific stats
    total_predictions = PredictionHistory.query.filter_by(user_id=current_user.id).count()
    
    avg_hdi = db.session.query(db.func.avg(PredictionHistory.predicted_hdi)).filter_by(user_id=current_user.id).scalar()
    avg_hdi = round(avg_hdi, 3) if avg_hdi else 0.0
    
    recent_predictions = PredictionHistory.query.filter_by(user_id=current_user.id).order_by(PredictionHistory.timestamp.desc()).limit(5).all()
    
    # Global stats
    active_model = ModelMetadata.query.filter_by(is_active=True).first()
    
    # Data for charts (Category distribution)
    categories = ['Very High', 'High', 'Medium', 'Low']
    category_counts = []
    for cat in categories:
        count = PredictionHistory.query.filter_by(user_id=current_user.id, predicted_category=cat).count()
        category_counts.append(count)
        
    chart_data = {
        'labels': categories,
        'data': category_counts
    }
    
    return render_template('dashboard.html', 
                           total_predictions=total_predictions, 
                           avg_hdi=avg_hdi, 
                           recent_predictions=recent_predictions,
                           active_model=active_model,
                           chart_data=chart_data)
