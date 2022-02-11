from celery import shared_task

@shared_task
def add_task(x, y):
    return x + y

@shared_task
def sub_task(x, y):
    return x - y

@shared_task
def mul_task(x, y):
    return x * y

@shared_task
def div_task(x, y):
    return x / y

