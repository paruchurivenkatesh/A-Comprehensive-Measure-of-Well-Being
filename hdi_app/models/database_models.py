from datetime import datetime
from hdi_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(64), default='Student') # Admin, Researcher, Policy Maker, Student
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    predictions = db.relationship('PredictionHistory', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def is_admin(self):
        return self.role == 'Admin'
        
    def __repr__(self):
        return f'<User {self.username}>'

class PredictionHistory(db.Model):
    __tablename__ = 'prediction_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Inputs
    country = db.Column(db.String(128), nullable=False)
    life_expectancy = db.Column(db.Float, nullable=False)
    mean_years_schooling = db.Column(db.Float, nullable=False)
    expected_years_schooling = db.Column(db.Float, nullable=False)
    gni_per_capita = db.Column(db.Float, nullable=False)
    
    # Outputs
    predicted_hdi = db.Column(db.Float, nullable=False)
    predicted_category = db.Column(db.String(64), nullable=False)
    
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Prediction {self.country} - {self.predicted_category}>'

class ModelMetadata(db.Model):
    __tablename__ = 'model_metadata'
    
    id = db.Column(db.Integer, primary_key=True)
    algorithm_name = db.Column(db.String(128), nullable=False)
    r2_score = db.Column(db.Float, nullable=False)
    mae = db.Column(db.Float, nullable=False)
    mse = db.Column(db.Float, nullable=False)
    rmse = db.Column(db.Float, nullable=False)
    training_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<ModelMetadata {self.algorithm_name} R2:{self.r2_score}>'
