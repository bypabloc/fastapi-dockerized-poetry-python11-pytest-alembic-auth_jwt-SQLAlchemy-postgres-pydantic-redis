"""
This script is used to initialize the database with initial data.

Path: app/scripts/initial_data.py
"""

import logging
import asyncio


from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.init_db import init_db
from app.db.main import Database
from app.config.database import settings_database as settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
DB_URI = settings.DB_URI

db = Database(DB_URI)


async def init() -> None:
    """Initialize the database, retrying if it's not ready yet."""
    async with db.get_db() as session:
        await init_db(session)


def main() -> None:
    """Initialize the service."""
    logger.info("Creating initial data")
    asyncio.run(init())
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
