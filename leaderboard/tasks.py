from __future__ import absolute_import

from celery import shared_task


@shared_task
def add(x, y): #, name='bubitest.tasks.add'):
    return x + y


@shared_task
def mul(x, y): #, name='bubitest.tasks.mul'):
    return x * y


@shared_task
def xsum(numbers): #, name='bubitest.tasks.xsum'):
    return sum(numbers)
