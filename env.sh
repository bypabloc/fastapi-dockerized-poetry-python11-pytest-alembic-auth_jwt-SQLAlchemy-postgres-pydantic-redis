#!/bin/sh

# File to generate env variables for the container
# Path: env.sh

echo "Generating env.sh..."

# Cargar las variables de entorno desde .env al shell actual
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Establecer valores por defecto para las variables si no están definidas
DB_DRIVER=${DB_DRIVER:-postgresql+asyncpg}
DB_USERNAME=${DB_USERNAME:-postgres}
DB_PASSWORD=${DB_PASSWORD:-123456}
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}
DB_NAME=${DB_NAME:-test_db}
DB_HOST_EXTERNAL=${DB_HOST_EXTERNAL:-$DB_HOST}
DB_PORT_EXTERNAL=${DB_PORT_EXTERNAL:-$DB_PORT}

# Si DB_URI no está definido, construye el DB_URI a partir de las otras variables
if [ -z "$DB_URI" ]; then
    DB_URI="${DB_DRIVER}://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
fi

# Mostrar las variables para verificar (esto es opcional)
echo "DB_DRIVER=$DB_DRIVER"
echo "DB_USERNAME=$DB_USERNAME"
echo "DB_PASSWORD=$DB_PASSWORD"
echo "DB_HOST=$DB_HOST"
echo "DB_PORT=$DB_PORT"
echo "DB_NAME=$DB_NAME"
echo "DB_URI=$DB_URI"
echo "DB_PORT_EXTERNAL=$DB_PORT_EXTERNAL"
echo "DB_HOST_EXTERNAL=$DB_HOST_EXTERNAL"

export DB_DRIVER
export DB_USERNAME
export DB_PASSWORD
export DB_HOST
export DB_PORT
export DB_NAME
export DB_URI
export DB_PORT_EXTERNAL
export DB_HOST_EXTERNAL
