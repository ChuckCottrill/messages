# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

from settings import env

# see env for ENV variables:
# DBENGINE
# PGHOST
# PGPORT
# PGNAME
# PGUSER
# PGPASSWORD

DATABASES = {
    "default": {
        "ENGINE": env(DBENGINE, default="django.db.backends.postgresql_psycopg2"),
        "HOST": env(PGHOST, defaults="localhost"),
        "PORT": env(PGPORT, defaults="5432"),
        "NAME": env(PGNAME, defaults="postgres"),
        "USER": env(PGUSER, defaults="user"),
        "PASSWORD": env(PGPASSWORD, defaults="password"),
    },
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": env(SQLITE, default=f"{BASE_DIR}/db.sqlite3"),
    },
    "cache": {
        "ENGINE": "django.db.backends.redis???",
        "NAME": env(CACHEDB, default="redis"),
    },
}

