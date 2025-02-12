import os 
from celery import Celery
from django.conf import settings

# set the default django setting module
os. environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsaggregator.settings')

# create a celery instance
app = Celery('newsaggregator')

# from all registered django apps they can load task module
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover tasks in all installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    