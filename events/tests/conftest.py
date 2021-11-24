from unittest.mock import Mock

import pytest

from events.models import Application
from events.serializers import EventSerializer


@pytest.fixture
def mocked_request():
    return Mock(META={'HTTP_AUTHORIZATION': ''})


@pytest.fixture
def new_application():
    return Application.objects.create(name='foo')


@pytest.fixture
def event_serializer(new_application, request):
    data = request.param
    return EventSerializer(data=data, app=new_application)
