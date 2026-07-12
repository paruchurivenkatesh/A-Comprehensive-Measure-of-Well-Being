import os
from hdi_app import create_app
from hdi_app.database.init_db import initialize_database

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    # Initialize database when running locally
    with app.app_context():
        initialize_database()
    app.run(debug=True, host='0.0.0.0', port=5000)
