from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from hdi_app.models.database_models import PredictionHistory
from hdi_app import db

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/history')
@login_required
def history():
    page = request.args.get('page', 1, type=int)
    # Paginate predictions
    predictions = PredictionHistory.query.filter_by(user_id=current_user.id)\
        .order_by(PredictionHistory.timestamp.desc())\
        .paginate(page=page, per_page=10)
        
    return render_template('history.html', predictions=predictions)
    
@reports_bp.route('/history/delete/<int:id>', methods=['POST'])
@login_required
def delete_history(id):
    prediction = PredictionHistory.query.get_or_404(id)
    if prediction.user_id != current_user.id:
        flash('You are not authorized to delete this record.', 'danger')
        return redirect(url_for('reports.history'))
        
    db.session.delete(prediction)
    db.session.commit()
    flash('Prediction record deleted successfully.', 'success')
    return redirect(url_for('reports.history'))

import csv
from flask import Response
from io import StringIO

@reports_bp.route('/report/download/csv')
@login_required
def download_csv():
    predictions = PredictionHistory.query.filter_by(user_id=current_user.id).order_by(PredictionHistory.timestamp.desc()).all()
    
    def generate():
        data = StringIO()
        writer = csv.writer(data)
        writer.writerow(['Date', 'Country', 'Life Expectancy', 'Mean Years Schooling', 'Expected Years Schooling', 'GNI Per Capita', 'Predicted HDI', 'Category'])
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)
        
        for p in predictions:
            writer.writerow([
                p.timestamp.strftime('%Y-%m-%d %H:%M'),
                p.country,
                p.life_expectancy,
                p.mean_years_schooling,
                p.expected_years_schooling,
                p.gni_per_capita,
                p.predicted_hdi,
                p.predicted_category
            ])
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    response = Response(generate(), mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="hdi_predictions_report.csv")
    return response

@reports_bp.route('/report/view')
@login_required
def view_report():
    predictions = PredictionHistory.query.filter_by(user_id=current_user.id).order_by(PredictionHistory.timestamp.desc()).all()
    return render_template('report.html', predictions=predictions)
