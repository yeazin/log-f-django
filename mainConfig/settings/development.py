from .base import *


ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

## APP installed
INSTALLED_APPS += [
    # third party apps
    "rest_framework",
    "accounts.apps.AccountsConfig",
]

## Custom User model Config
AUTH_USER_MODEL = "accounts.User"
