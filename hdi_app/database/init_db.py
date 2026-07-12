from hdi_app import db, create_app
from hdi_app.models.database_models import User
from werkzeug.security import generate_password_hash
import os

def initialize_database():
    """Create database tables and insert a default admin user if one doesn't exist."""
    db.create_all()
    
    # Check if admin user exists
    admin_user = User.query.filter_by(email='admin@hdi.org').first()
    if not admin_user:
        print("Creating default admin user...")
        admin = User(
            username='Admin',
            email='admin@hdi.org',
            password_hash=generate_password_hash('admin123'),
            role='Admin'
        )
        db.session.add(admin)
        db.session.commit()
        print("Default admin created (admin@hdi.org / admin123).")
