from django.core.exceptions import ImproperlyConfigured

from .base import *

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("ALLOWED_HOSTS must be set in production")

DATABASE_URL = env("DATABASE_URL", default=None)
if not DATABASE_URL:
    raise ImproperlyConfigured("DATABASE_URL must be set in production")

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# TODO: For now allow all CORS origin
CORS_ALLOW_ALL_ORIGINS = True

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": env("STORAGE_BUCKET_NAME"),
            "access_key": env("STORAGE_ACCESS_KEY_ID"),
            "secret_key": env("STORAGE_ACCESS_KEY"),
            "endpoint_url": env("STORAGE_ENDPOINT_URL"),
            "region_name": "auto",
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

MEDIA_URL = env("MEDIA_URL", default=None)
if not MEDIA_URL:
    endpoint = env("STORAGE_ENDPOINT_URL")
    bucket = env("STORAGE_BUCKET_NAME")
    MEDIA_URL = f"{endpoint.rstrip('/')}/{bucket}/"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
