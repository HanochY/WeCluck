from app.init_app import app
from backend.src.dbs.main.db_manager import db_manager

with app.app_context():
    db_manager.init_db(app)
    app.run()