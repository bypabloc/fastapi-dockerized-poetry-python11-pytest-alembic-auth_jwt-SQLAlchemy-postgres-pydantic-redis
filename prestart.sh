#! /usr/bin/env bash

# Let the DB start
python ./app/scripts/backend_pre_start.py

# # Run migrations
# alembic upgrade head

# # Create initial data in DB
# python ./app/scripts/initial_data.py
