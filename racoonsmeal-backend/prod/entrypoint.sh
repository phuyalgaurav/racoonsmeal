#!/bin/sh
set -euo pipefail

if [ "${MIGRATE_ON_START:-0}" = "1" ]; then
	python src/manage.py migrate
fi

if [ "${COLLECTSTATIC_ON_START:-1}" = "1" ]; then
	python src/manage.py collectstatic --noinput
fi

exec gunicorn \
	config.wsgi:application \
	--bind 0.0.0.0:8000 \
	--workers "${GUNICORN_WORKERS:-3}" \
	--threads "${GUNICORN_THREADS:-2}" \
	--timeout "${GUNICORN_TIMEOUT:-30}" \
	--max-requests 2000 \
	--max-requests-jitter 200