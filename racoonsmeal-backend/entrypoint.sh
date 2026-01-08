#!/bin/sh
set -euo pipefail

python src/manage.py makemigrations
python src/manage.py migrate

exec python src/manage.py runserver 0.0.0.0:8000