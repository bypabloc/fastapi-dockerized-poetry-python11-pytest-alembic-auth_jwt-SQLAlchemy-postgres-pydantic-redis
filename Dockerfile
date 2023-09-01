# Path: ./Dockerfile

# pull the official docker image
FROM python:3.11.1-slim as base

# create the app user with specific UID and GID
RUN addgroup --system --gid 1000 app && adduser --system --uid 1000 --group app

# set work directory
WORKDIR /app

# ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs)
# in real time. Equivalent to python -u: https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TESTING 0

# Install Poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock ./

# # Allow installing dev dependencies to run tests
# ARG INSTALL_DEV=false

# RUN echo "Valor de INSTALL_DEV: $INSTALL_DEV"
# RUN if [ "$INSTALL_DEV" = "true" ]; then poetry install --no-root; else poetry install --no-root --no-dev; fi

RUN poetry install --no-root

# Cambia a usuario root para asegurarte de que tienes los permisos necesarios para cambiar los permisos del script
USER root

# Copia todos los archivos
COPY . .

# Cambia los permisos del script
RUN chmod +x run.sh

# Cambiar permisos de la carpeta "app/migrations/versions"
RUN chmod -R 777 ./migrations/versions

# Lista los archivos para ver sus permisos
RUN ls -l

ENV PYTHONPATH=./

# chown all the files to the app user
RUN chown -R app $HOME

# change to the app user
# Switch to a non-root user, which is recommended by Heroku.
USER app

# Ejecuta el script
CMD ["bash", "/app/run.sh"]
