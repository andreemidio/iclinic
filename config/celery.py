import os

from celery import Celery
# Set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('iclinic')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.

app = Celery('iclinic',
             broker=settings.CLOUDAMQP_URL,
             )

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
