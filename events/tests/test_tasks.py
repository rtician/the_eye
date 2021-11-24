import uuid

import pytest

from events.models import Application, Event, Session
from events.tasks import create_event


@pytest.mark.django_db
def test_create_event():
    assert 0 == Event.objects.all().count()

    app = Application.objects.create(name='foo')
    session = Session.objects.create(id=uuid.uuid4(), app=app)

    payload = {
        'session_id': session.id,
        'name': 'pageview',
        'category': 'page interaction',
        'data': {
            'host': 'www.consumeraffairs.com',
            'path': '/',
        },
        'timestamp': '2021-01-01 09:15:27.243860',
    }
    create_event(payload)
    assert 1 == Event.objects.all().count()

    Event.objects.all().delete()
    session.delete()
    app.delete()
