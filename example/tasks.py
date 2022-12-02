from celery import shared_task
from time import sleep


@shared_task
def adding_task(x, y):
    return x + y


@shared_task
def sleepy(duration):
    sleep(duration)
    return None
