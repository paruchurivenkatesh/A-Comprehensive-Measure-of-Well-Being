import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-hdi-project-2026'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Path settings
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'dataset')
    MODELS_DIR = os.path.join(BASE_DIR, 'models')
    
    # Create necessary directories
    os.makedirs(os.path.join(DATA_DIR, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(DATA_DIR, 'processed'), exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'hdi_app', 'static', 'images', 'eda'), exist_ok=True)

class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(Config.BASE_DIR, 'hdi_app', 'database', 'hdi_dev.db')
    os.makedirs(os.path.join(Config.BASE_DIR, 'hdi_app', 'database'), exist_ok=True)

class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(Config.BASE_DIR, 'hdi_app', 'database', 'hdi_prod.db')

# Dictionary to easily select configuration
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
