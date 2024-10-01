from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config.provider import ConfigProvider
from src.dal.dbs.forum.db_manager import init_db
from routes.user import users_blueprint
from routes.topic import topics_blueprint
from routes.authentication import authentication_blueprint
from routes.comment import comments_blueprint
from routes.preflight import preflight_blueprint


@asynccontextmanager
async def lifespan(instance: FastAPI):
    _ = instance
    await init_db()
    yield
    
app_settings = ConfigProvider.forum_settings()
db_settings = ConfigProvider.forum_db_settings()
app_metadata = ConfigProvider.metadata()

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