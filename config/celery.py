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


# Load task modules from all registered Django apps.

app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    #Scheduler Name
    'print-message-ten-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'print_msg_main',  
        # Schedule      
        'schedule': 10.0,
        # Function Arguments 
    },
    #Scheduler Name
    'print-time-twenty-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'print_time',  
        # Schedule      
        'schedule': 20.0, 
    },
}  

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


