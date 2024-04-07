
from config.app import app

from routes.comments import comments_blueprint
from routes.users import users_blueprint
from routes.preflight import preflight_blueprint
from routes.topics import topics_blueprint
from init_db import init_db

app.register_blueprint(comments_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(preflight_blueprint)
app.register_blueprint(topics_blueprint)

with app.app_context():
    init_db()
    app.run(debug=True)
    