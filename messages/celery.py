
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messages.settings")

celery_app = Celery("messages")
celery_app.config_from_object("djgango.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

