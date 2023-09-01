import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def convert_variable(value):
    """
    Convierte una variable de entorno a un tipo de dato
    """
    # Intentamos convertir a integer
    try:
        return int(value)
    except ValueError:
        pass

    # Intentamos convertir a float
    try:
        return float(value)
    except ValueError:
        pass

    # Intentamos convertir a dict
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        pass

    # Intentamos convertir a list
    try:
        # Asumiendo que la lista viene en formato JSON
        return json.loads(value)
    except json.JSONDecodeError:
        pass

    # Si no es convertible, retornamos la misma variable
    return value


class EnvVar:
    """
    Clase para obtener variables de entorno
    """
    def __getattr__(self, name):
        # Intenta obtener la variable de entorno con el nombre especificado
        get_env = os.environ.get(name.upper())

        if get_env is None:
            return None

        # Intenta convertir la variable de entorno a un tipo de dato
        get_env = convert_variable(get_env)

        # Guarda la variable de entorno como un atributo en el objeto
        setattr(self, name, get_env)

        # Devuelve el valor de la variable de entorno
        return get_env


# Uso del modelo
env_var = EnvVar()
