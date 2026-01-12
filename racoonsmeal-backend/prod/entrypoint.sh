#!/bin/sh
set -euo pipefail

python src/manage.py makemigrations
python src/manage.py migrate
python src/manage.py collectstatic --noinput

exec "gunicorn" "config.wsgi:application" --bind 0.0.0.0:8000