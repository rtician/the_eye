from __future__ import absolute_import

from celery import Celery
from django.conf import settings

celery_app = Celery('the_eye')

celery_app.conf.update(
    broker_url=settings.BROKER_URL,
    accept_content=['json'],
    task_serializer='json',
)
celery_app.autodiscover_tasks()
