from .base import *

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

DEBUG = False

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

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
