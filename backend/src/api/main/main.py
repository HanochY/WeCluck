from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config.provider import ConfigProvider
from routes.user import router as user_router
from routes.topic import router as topic_router
from routes.authentication import router as authentication_router
from routes.comment import router as comment_router
#from routes.preflight import preflight_blueprint

    
app_settings = ConfigProvider.forum_settings()
app_metadata = ConfigProvider.metadata()

app = FastAPI(root_path="/api",
              title=app_metadata.PROJECT_NAME,
              description=app_metadata.PROJECT_DESCRIPTION,
              version=app_metadata.VERSION,
              responses={404: {"description": "Not found"}})

if app_settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            app_settings.CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

app.include_router(user_router)
app.include_router(topic_router)
app.include_router(authentication_router)
app.include_router(comment_router)