from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import AnyHttpUrl
from pydantic import EmailStr
from pydantic import HttpUrl
from pydantic import PostgresDsn
from pydantic import validator
from pydantic_settings import BaseSettings

from app.utils.env_var import env_var


class Settings(BaseSettings):
    """
    Settings class.
    """
    PROJECT_VERSION: str = "1.0.0"

    API_V1_STR: str = "/v1"

    ENVIRONMENT: str = env_var.ENVIRONMENT

    @validator("ENVIRONMENT", pre=True)
    @classmethod
    def get_environment(cls, value: str | None) -> str:
        """Get the environment"""
        if value is None:
            return "local"
        if value not in ["local", "dev", "prod"]:
            raise ValueError(f"Invalid environment: {value}")
        return value

    SECRET_KEY: str = env_var.SECRET_KEY
    ALGORITHM: str = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    PROJECT_NAME: str = "Project X"
    SERVER_HOST: AnyHttpUrl

    BACKEND_CORS_METHODS: List = env_var.BACKEND_CORS_METHODS
    BACKEND_CORS_HEADERS: List = env_var.BACKEND_CORS_HEADERS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = env_var.BACKEND_CORS_ORIGINS

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    @classmethod
    def assemble_cors_origins(cls, value: Union[str, List[str]]) -> Union[List[str], str]:
        """Assemble CORS origins"""
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]
        elif isinstance(value, (list, str)):
            return value
        raise ValueError(value)

    SENTRY_DSN: HttpUrl | None = None

    @validator("SENTRY_DSN", pre=True)
    @classmethod
    def sentry_dsn_can_be_blank(cls, value: Optional[str]) -> Optional[str]:
        """Sentry DSN can be blank"""
        if value is None or len(value) == 0:
            return None
        return value

    SMTP_TLS: bool = True
    SMTP_PORT: int | None = None
    SMTP_HOST: str | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAILS_FROM_EMAIL: EmailStr | None = None
    EMAILS_FROM_NAME: str | None = None

    @validator("EMAILS_FROM_NAME")
    @classmethod
    def get_project_name(cls, value: Optional[str], values: Dict[str, Any]) -> str:
        """If EMAILS_FROM_NAME is not set, use PROJECT_NAME"""
        if not value:
            return values["PROJECT_NAME"]
        return value

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    @classmethod
    def get_emails_enabled(cls, _value: bool, values: Dict[str, Any]) -> bool:
        """Set EMAILS_ENABLED to True if all SMTP settings were provided."""
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"
    FIRST_SUPERUSER: EmailStr | None = env_var.FIRST_SUPERUSER
    FIRST_SUPERUSER_PASSWORD: str | int = env_var.FIRST_SUPERUSER_PASSWORD
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        """Config for pydantic-settings"""
        case_sensitive = True


try:
    settings = Settings()
except Exception as e:
    raise e
