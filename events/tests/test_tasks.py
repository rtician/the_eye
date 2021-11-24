import pytest

from events.models import Event
from events.tasks import create_event


@pytest.mark.django_db
def test_create_event(session):
    assert 0 == Event.objects.all().count()

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
