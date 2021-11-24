import uuid
from unittest.mock import Mock

import pytest
from rest_framework.test import APIClient

from events.models import Application, Session
from events.serializers import EventSerializer


@pytest.fixture
def mocked_request():
    return Mock(META={'HTTP_AUTHORIZATION': ''})


@pytest.fixture
def application():
    app = Application.objects.create(name='foo')
    yield app
    app.delete()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def session(application):
    session = Session.objects.create(id=uuid.uuid4(), app=application)
    yield session
    session.delete()


@pytest.fixture
def event_serializer(application, request):
    data = request.param
    return EventSerializer(data=data, app=application)
