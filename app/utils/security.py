from datetime import datetime
from datetime import timedelta
from typing import Any

from jwt import encode
from bcrypt import hashpw
from bcrypt import gensalt
from bcrypt import checkpw

from app.config.setting import settings


def create_access_token(
    subject: str | Any,
    expires_delta: timedelta = None,
) -> str:
    """
    Crear un token de acceso
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(hashed_password: str, input_password: str):
    """
    Verificar si la contraseña encriptada coincide con la contraseña ingresada
    """
    return checkpw(input_password.encode('utf-8'), hashed_password)


def get_password_hash(password: str):
    """
    Encriptar la contraseña
    """
    salt = gensalt()
    # Generar el hash en bytes
    hashed_password_bytes = hashpw(password.encode('utf-8'), salt)

    # Convertir el hash de bytes a cadena
    hashed_password_str = hashed_password_bytes.decode('utf-8')

    return hashed_password_str
