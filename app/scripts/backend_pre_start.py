"""
Este script se ejecuta antes de iniciar el servidor de la API.

Se utiliza para asegurarse de que la base de datos esté lista para aceptar conexiones.

Path: app/scripts/backend_pre_start.py
"""

import asyncio
import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from sqlalchemy import text

from app.db.main import Base as DBBase
from app.db.main import Database
from app.config.database import settings_database as settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


MAX_TRIES = int(settings.MAX_TRIES)
WAIT_SECONDS = int(settings.WAIT_SECONDS)
DB_URI = settings.DB_URI

db = Database(DB_URI)


@retry(
    stop=stop_after_attempt(MAX_TRIES),
    wait=wait_fixed(WAIT_SECONDS),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init() -> None:
    """Initialize the database, retrying if it's not ready yet."""
    try:
        async with db.get_db() as session:
            await session.execute(text("SELECT 1"))
    except Exception as e:  # Sería bueno capturar excepciones más específicas
        logger.error(f"An error occurred: {e}")
        raise


def main() -> None:
    """Initialize the service."""
    logger.info("Initializing service")
    asyncio.run(init())
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
