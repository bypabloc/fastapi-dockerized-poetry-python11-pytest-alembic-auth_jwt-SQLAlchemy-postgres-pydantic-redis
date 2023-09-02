"""
Ping endpoint.

Path: app/api/v1/endpoints/ping.py

Route: /v1/ping/
"""

from typing import Any

from fastapi import APIRouter

from app.utils.logger import CustomLogger


logger = CustomLogger(__name__)

router = APIRouter()


@router.get("/")
def pong():
    """
    Ping endpoint.
    """
    return {"ping": "pong!"}
