#!/Users/chuck/me/code/messages/env/bin/python3
from django_redis import get_redis_connection

def tearDown(self):
    get_redis_connection("default").flushall()

