from config.app import app

from routes.comments import comments_blueprint
from routes.users import users_blueprint


app.register_blueprint(comments_blueprint)
app.register_blueprint(users_blueprint)


with app.app_context():
    app.run(debug=True)