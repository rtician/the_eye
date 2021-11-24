from events.models import Event
from the_eye import celery_app


@celery_app.task(name='the_eye.create_event')
def create_event(payload):
    Event.objects.create(**payload)
