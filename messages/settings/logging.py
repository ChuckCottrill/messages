# configure logging parameters
# https://docs.djangoproject.com/en/4.0/topics/logging/

# import os
import sys

from messages.settings import env

DFLT_LOG_FORMAT  = "[%(asctime)s] [%(levelname)s] [%(name)s|%(funcName)s|%(lineno)s|%(thread)s] %(message)s"
# name? module/filename funcName lineno thread threadName
DFLT_LOG_SIMPLE  = "[%(asctime)s] [%(levelname)s] %(message)s"
DFLT_LOG_DATEFMT = "%Y-%m-%dT%H:%M:%S%z"

LOG_LEVEL = env("LOG_LEVEL", default="INFO")
LOG_FORMAT  = env("LOG_FORMAT", default=DFLT_LOG_FORMAT)
LOG_SIMPLE  = env("LOG_SIMPLE", default=DFLT_LOG_SIMPLE)
LOG_DATEFMT = env("LOG_DATEFMT", default=DFLT_LOG_DATEFMT)

def logger_handlers() -> []:
    if env("LOG_LEVEL", default="INFO") != DEBUG:
        return ["console"]
    else:
        return ["debug"]

LOGGING = {
    "version": 1,
    "disabble_existing_loggers": False,
    "formatters": {
        "console": {
            "format": LOG_FORMAT,
            "datefmt": LOG_DATEFMT,
        },
        "debug": {
            "format": LOG_FORMAT,
            "datefmt": LOG_DATEFMT,
        },
        "verbose": {
            "format": LOG_FORMAT,
            "datefmt": LOG_DATEFMT,
        },
        "simple": {
            "format": LOG_SIMPLE,
            "datefmt": LOG_DATEFMT,
        },
    },
    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "console",
        },
        "debug": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "debug",
        },
         "null": {
             "level": "DEBUG",
             "class": "logging.NullHandler",
             # "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "level": LOG_LEVEL,
            "handlers": logger_handlers(),
            "propagate": True,
        },
        "django.request": {
            "level": "ERROR",
            "handlers": logger_handlers(),
            "propagate": False,
        },
        "gunicorn": {
            "level": LOG_LEVEL,
            "handlers": logger_handlers(),
            "propagate": True,
        },
        # turn off auto-reload messages (they happen at DEBUG level)
        "django.utils.autoreload": {
            "level": "INFO",
            "handlers": logger_handlers(),
            "propagate": False,
        },
        "messages": {
            "level": LOG_LEVEL,
            "handlers": logger_handlers(),
            "propagate": True,
        },
        "api": {
            "level": LOG_LEVEL,
            "handlers": logger_handlers(),
            "propagate": True,
        },
        "cars": {
            "level": LOG_LEVEL,
            "handlers": logger_handlers(),
            "propagate": True,
        },
        "polls": {
            "level": LOG_LEVEL,
            "handlers": logger_handlers(),
            "propagate": True,
        },
    },
    "root": {
        # "level": LOG_LEVEL,
        "level": "WARNING",
        "handlers": ["console"],
        # "propagate": True,
    },
}

