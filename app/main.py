from fastapi import FastAPI
from fastapi import Depends
from starlette.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import Response

from app.api.v1.routes import api_router
from app.config.setting import settings
from app.utils.logger import CustomLogger
from app.db.main import db

logger = CustomLogger(__name__)

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


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Startup event
    """
    logger.info("Starting up...")
    db.connect()
    logger.info("Startup completed")


# Log response status code and body
@app.middleware("http")
async def log_response(request: Request, call_next):
    """
    Log response status code and body
    """
    response = await call_next(request)
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
        )
    ]
)
