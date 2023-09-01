"""
File to start the application

This file is responsible for starting the application and
setting up the database connection.

Path: app/main.py
"""
import time

from fastapi import FastAPI
from fastapi import Depends
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request
from fastapi.responses import Response

from app.api.v1.routes import api_router
from app.config.setting import settings
from app.utils.logger import CustomLogger
from app.db.main import Database
from app.config.database import settings_database

logger = CustomLogger(__name__)
DB_URI = settings_database.DB_URI
db = Database(DB_URI)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


# Logs incoming request information
async def log_request(request: Request):
    """
    Log request information
    """
    logger.info(
        f"[{request.client.host}:{request.client.host}] {request.method} {request.url}"
    )
    logger.info(f"header: {request.headers}, body: ")
    logger.info(await request.body())


class CORSMiddleware(BaseHTTPMiddleware):
    """
    Middleware to allow CORS
    """
    async def dispatch(self, request: Request, call_next):
        """
        Dispatch method
        """
        response = await call_next(request)

        origins = ", ".join(str(origin) for origin in settings.BACKEND_CORS_ORIGINS)
        methods = ", ".join(str(method) for method in settings.BACKEND_CORS_METHODS)
        headers = ", ".join(str(header) for header in settings.BACKEND_CORS_HEADERS)

        response.headers['Access-Control-Allow-Origin'] = origins
        response.headers['Access-Control-Allow-Methods'] = methods
        response.headers['Access-Control-Allow-Headers'] = headers

        return response


app.add_middleware(
    CORSMiddleware,
)


# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Startup event
    """
    logger.info("Startup completed")


# Shutdown event
@app.on_event("shutdown")
async def shutdown():
    """
    Shutdown event
    """
    await db.disconnect()


# Log response status code and body
@app.middleware("http")
async def log_response(request: Request, call_next):
    """
    Log response status code and body
    """
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    logger.info(f"{response.status_code} {body}")

    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
    )

app.include_router(
    api_router,
    prefix=settings.API_V1_STR,
    dependencies=[
        Depends(
            log_request
        ),
    ]
)
