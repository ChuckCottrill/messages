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

# database engines available:
# "django.db.backends.postgresql",
# "django.db.backends.mysql",
# "django.db.backends.sqlite3",
# "django.db.backends.oracle",
# "django.db.backends.redis",

REDISHOST = env(REDISHOST, default="localhost") # "127.0.0.1"
REDISPORT = env(REDISPORT, default="6379")

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
        "ENGINE": "django.db.backends.redis???", # "django_redis.cache.RedisCache",
        "NAME": env(CACHEDB, default=f"redis://{REDISHOST}/{REDISPORT}/0"),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDISHOST}:{REDISPORT}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

