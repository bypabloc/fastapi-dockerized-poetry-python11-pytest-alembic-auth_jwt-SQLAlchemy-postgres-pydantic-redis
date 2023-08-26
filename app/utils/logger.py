"""
Módulo para el manejo de logs
"""

from logging import Formatter as LogFormatter
from logging import getLogger as log_getLogger
from logging import StreamHandler as LogStreamHandler
from logging import DEBUG as LogDebug
from logging import INFO as LogInfo
from sys import stdout as sys_stdout
from app.config.setting import settings


# Colores para cada nivel de registro
COLORS = {
    'INFO': '\033[94m',
    'DEBUG': '\033[92m',
    'WARNING': '\033[93m',
    'ERROR': '\033[91m',
    'CRITICAL': '\033[95m',
    'ENDC': '\033[0m'
}


class ColoredFormatter(LogFormatter):
    """
    Formato personalizado para el logger
    """
    def format(self, record):
        log_message = super().format(record)
        return f"{COLORS.get(record.levelname, COLORS['ENDC'])}{log_message}{COLORS['ENDC']}"


class CustomLogger:
    """
    Clase para el manejo de logs
    """
    def __init__(self, name: str):
        environment = settings.ENVIRONMENT
        self.logger = log_getLogger(name)
        self.logger.setLevel(LogDebug if environment != "prod" else LogInfo)
        console_format = LogStreamHandler(sys_stdout)
        formatter = ColoredFormatter(
            "[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_format.setFormatter(formatter)
        self.logger.addHandler(console_format)
        self.environment = environment

    def custom_log(self, level, *args):
        """
        Log a message with severity 'level' on the logger corresponding to this
        custom logger. If the logger has no such handler, the message is ignored.
        """
        msg_parts = []
        for arg in args:
            if isinstance(arg, dict):
                msg_parts.append(self.format_dict(arg))
            elif hasattr(arg, '__dict__'):
                msg_parts.append(self.format_object(arg))
            else:
                msg_parts.append(str(arg))
        msg = " ".join(msg_parts)
        getattr(self.logger, level)(msg)

    @staticmethod
    def format_dict(obj):
        """
        Formatea un diccionario para que se vea bien en el log
        """
        return "\n" + "\n".join([f"  {k}: {v}" for k, v in sorted(obj.items())])

    @staticmethod
    def format_object(obj):
        """
        Formatea un objeto para que se vea bien en el log
        """
        if hasattr(obj, '__dict__'):
            return CustomLogger.format_dict(obj.__dict__)
        return str(obj)

    def info(self, *args):
        """
        Log a message with severity 'INFO' on the logger corresponding to this
        custom logger. If the logger has no such handler, the message is ignored.
        """
        if self.environment != "prod":
            self.custom_log('info', *args)

    def debug(self, *args):
        """
        Log a message with severity 'DEBUG' on the logger corresponding to this
        custom logger. If the logger has no such handler, the message is ignored.
        """
        if self.environment == "dev":
            self.custom_log('debug', *args)

    def warn(self, *args):
        """
        Log a message with severity 'WARNING' on the logger corresponding to this
        custom logger. If the logger has no such handler, the message is ignored.
        """
        if self.environment == "dev":
            self.custom_log('warning', *args)

    def error(self, *args):
        """
        Log a message with severity 'ERROR' on the logger corresponding to this
        custom logger. If the logger has no such handler, the message is ignored.
        """
        self.custom_log('error', *args)
