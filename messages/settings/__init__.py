### app/settings/init.py

import os
import sys
from pathlib import Path

from environs import Env
from split_settings.tools import optional, include

env = Env()
# set project base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# or is it...
# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR: {BASE_DIR}")

# read environment variables from .env file
# env.read_env(os.path.join(BASE_DIR, ".env")
env.read_env()

# ENV(ronment) is one of [ DEV/LOCAL, QA, STAGE, PROD ]
# ENV = os.environ.get("ENV")
ENV = env("ENV", default="DEV")
DEBUG = env.bool("DEBUG", False)

envfile = "env/env.dev"
if ENV == "DEV":
    envfile = "env/env.dev"
if ENV == "LOCAL":
    envfile = "env/env.local"
if ENV == "QA":
    envfile = "env/env.qa"
if ENV == "STAGE":
    envfile = "env/env.stage"
if ENV == "PROD":
    envfile = "env/env.prod"

include(
    "base.py",
    "database.py",
    "logging.py",
    "internationalization.py",
    optional("env/celery.py"),
    optional("env/api.py"),
    optional("env/dev.py"),
    optional("env/local.py"),
    optional(envfile),
)



