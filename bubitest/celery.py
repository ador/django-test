from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bubitest.settings')

from django.conf import settings

app = Celery('bubitest_c2') # or 'django-test' ?

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#@app.task(bind=True) #, name='leaderboard.celery.debug_task')
#def debug_task(self):
    #print('Request: {0!r}'.format(self.request))

#@app.task(bind=True) #, name='leaderboard.celery.hello')
#def hello(self):
    #print('Hello: {0!r}'.format(self.request))

