

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
    }
}

