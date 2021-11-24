from unittest.mock import Mock

import pytest

from events.models import Application


@pytest.fixture
def mocked_request():
    return Mock(META={'HTTP_AUTHORIZATION': ''})


@pytest.fixture
def new_application():
    return Application.objects.create(name='foo')
