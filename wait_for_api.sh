#!/bin/bash
# wait_for_api.sh

set -e

host="$1"
shift
cmd="$@"

until curl -s "$host" > /dev/null; do
  >&2 echo "API is unavailable - sleeping"
  sleep 1
done

>&2 echo "API is up - executing command"
exec $cmd
