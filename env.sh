#!/bin/bash

# Declare an associative array to store the variables
declare -A env_vars

# Read the .env file line by line
while read -r line; do
  # Skip comments and empty lines
  [[ $line =~ ^#.*$ || -z $line ]] && continue

  # Extract key and value
  key=$(echo $line | cut -d '=' -f 1)
  value=$(echo $line | cut -d '=' -f 2-)

  # Clean the value if it's a JSON-like array
  if [[ $value =~ ^\[.*\]$ ]]; then
    # No need to clean, it's a valid JSON array
    :
  else
    value=$(echo $value | tr -d '[]"')
  fi

  # Store the key-value pair in the associative array
  env_vars[$key]=$value
done < .env

# Establecer valores por defecto para las variables si no están definidas
env_vars[DB_DRIVER]=${env_vars[DB_DRIVER]:-postgresql+asyncpg}
env_vars[DB_USERNAME]=${env_vars[DB_USERNAME]:-postgres}
env_vars[DB_PASSWORD]=${env_vars[DB_PASSWORD]:-123456}
env_vars[DB_HOST]=${env_vars[DB_HOST]:-db}
env_vars[DB_PORT]=${env_vars[DB_PORT]:-5432}
env_vars[DB_NAME]=${env_vars[DB_NAME]:-test_db}
env_vars[DB_HOST_EXTERNAL]=${env_vars[DB_HOST_EXTERNAL]:-DB_HOST}
env_vars[DB_PORT_EXTERNAL]=${env_vars[DB_PORT_EXTERNAL]:-DB_PORT}

if [[ -z "${env_vars[DB_URI]}" ]]; then
  env_vars[DB_URI]=${env_vars[DB_DRIVER]}://${env_vars[DB_USERNAME]}:${env_vars[DB_PASSWORD]}@${env_vars[DB_HOST]}:${env_vars[DB_PORT]}/${env_vars[DB_NAME]}
fi

env_vars[BACKEND_CORS_ORIGINS]=${env_vars[BACKEND_CORS_ORIGINS]:-["*"]}
env_vars[BACKEND_CORS_METHODS]=${env_vars[BACKEND_CORS_METHODS]:-["*"]}
env_vars[BACKEND_CORS_ALLOW_HEADERS]=${env_vars[BACKEND_CORS_ALLOW_HEADERS]:-["*"]}

# Export the variables to the environment
for key in "${!env_vars[@]}"; do
  export $key="${env_vars[$key]}"
done
