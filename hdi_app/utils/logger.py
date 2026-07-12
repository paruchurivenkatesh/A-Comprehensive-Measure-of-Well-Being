import logging
import os
from logging.handlers import RotatingFileHandler
from config import Config

def setup_logger(app):
    """Setup application logging."""
    log_dir = os.path.join(Config.BASE_DIR, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Set log file path
    log_file = os.path.join(log_dir, 'hdi_app.log')
    
    # Configure the log handler
    file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('HDI Predictor startup')
