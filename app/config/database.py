from pydantic import validator
from pydantic_settings import BaseSettings

from app.utils.env_var import env_var
from app.utils.logger import CustomLogger


logger = CustomLogger(__name__)


class SettingsDatabase(BaseSettings):
    """
    Settings class.
    """
    DB_USERNAME: str = env_var.DB_USERNAME
    DB_PASSWORD: str = env_var.DB_PASSWORD
    DB_HOST: str = env_var.DB_HOST
    DB_PORT: int = env_var.DB_PORT
    DB_NAME: str = env_var.DB_NAME

    DB_URI: str | None = env_var.DB_URI

    # @validator("DB_URI", pre=True)
    # @classmethod
    # def assemble_db_connection(cls, value: Optional[str], values: Dict[str, Any]) -> Any:
    #     """Assemble the DB connection"""
    #     logger.info("DB_URI is None, assembling it from DB_* env vars -----------------")
    #     logger.info(f"DB_URI: {value}")
    #     logger.info(f"postgresql://{values.get('DB_USERNAME')}:{values.get('DB_PASSWORD')}@{values.get('DB_HOST')}:{values.get('DB_PORT')}/{values.get('DB_NAME')}")

    #     if isinstance(value, str):
    #         return value
    #     return PostgresDsn.build(
    #         scheme="postgresql",
    #         username=values.get("DB_USERNAME"),
    #         password=values.get("DB_PASSWORD"),
    #         host=values.get("DB_HOST"),
    #         port=values.get("DB_PORT"),
    #         path=f"/{values.get('DB_NAME') or ''}",
    #     )

    class Config:
        """Config for pydantic-settings"""
        case_sensitive = True


try:
    settings_database = SettingsDatabase()
except Exception as e:
    logger.error(f"Error loading settings: {e}")
    raise e
