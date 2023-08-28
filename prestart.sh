#! /usr/bin/env bash

# This file contains commands that are run before the application starts.
# Useful for migrations and other preparation tasks.
# Path: prestart.sh


# Let the DB start
python ./app/scripts/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python ./app/scripts/initial_data.py
