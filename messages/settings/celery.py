# Celery

from settings import env

# ENV:
# CELERY_BROKER_URL
# CELERY_RESULT_BACKEND
# 
# RABBITMQ_PROTO
# RABBITMQ_HOST
# RABBITMQ_PORT
# RABBITMQ_VHOST
# RABBITMQ_USERNAME
# RABBITMQ_PASSWORD
# 

# Celery
CELERY_BROKER_URL = env(CELERY_BROKER_URL, default="redis://localhost:6379")
CELERY_RESULT_BACKEND = env(CELERY_RESULT_BACKEND, default="redis://localhost:6379")
CELERY_ACCEPT_CONTENT = env(CELERY_ACCEPT_CONTENT, default=["application/json"])
CELERY_RESULT_SERIALIZER = env(CELERY_RESULT_SERIALIZER, default="json")
CELERY_TASK_SERIALIZER = env(CELERY_TASK_SERIALIZER, default="json")

# RabbitMQ
RABBITMQ_PROTO = env("RABBITMQ_PROTO", default="needed")
RABBITMQ_HOST = env("RABBITMQ_HOST", default="localhost")
RABBITMQ_PORT = env("RABBITMQ_PORT", default="5672")
RABBITMQ_VHOST = env("RABBITMQ_VHOST", default="/")
RABBITMQ_USERNAME = env("RABBITMQ_USERNAME", default="guest")
RABBITMQ_PASSWORD = env("RABBITMQ_PASSWORD", default="guest")

RABBITMQ_BROKER = env(RABBITMQ_BROKER, default=f"redis://localhost:6379")
RABBITMQ_URL = env(RABBITMQ_URL, default=f"default:/localhost:5672")
RABBITMQ_GET_QUEUE = env(RABBITMQ_GET_QUEUE, default=f"api/queues")
RABBITMQ_API_HOST = env(RABBITMQ_API_HOST, default=f"api/queues")

