from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config.provider import ConfigProvider
from src.dal.dbs.forum.db_manager import init_forum_db
from api.routes.user import users_blueprint
from api.routes.topic import topics_blueprint
from api.routes.authentication import authentication_blueprint
from api.routes.comment import comments_blueprint
from api.routes.preflight import preflight_blueprint


@asynccontextmanager
async def lifespan(instance: FastAPI):
    _ = instance
    await init_forum_db()
    yield
    
app_settings = ConfigProvider.app_settings()
app_metadata = ConfigProvider.app_metadata()

app = FastAPI(root_path="/api",
              title=app_metadata.PROJECT_NAME,
              description=app_metadata.PROJECT_DESCRIPTION,
              version=app_metadata.VERSION,
              lifespan=lifespan,
              responses={404: {"description": "Not found"}})

app.register_blueprint(comments_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(preflight_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(topics_blueprint)



app.secret_key = app_settings.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = db_settings.SQLITE_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app_settings.TRACK_MODIFICATIONS
app.config['DEBUG'] = app_settings.DEBUG
app.config['SERVER_NAME'] = f"{app_settings.ADDRESS}:{app_settings.PORT}"
app.config['THREADED'] = app_settings.THREAD_COUNT > 1
#CORS(app, origins=app_settings.ALLOWED_ORIGINS)