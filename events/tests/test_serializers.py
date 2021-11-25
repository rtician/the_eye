from unittest.mock import patch

import pytest

from events.models import Session

VALID_DATA = {
    'name': 'foo',
    'category': 'foo',
    'data': {},
    'timestamp': '2021-01-01 09:15:27.243860',
    'session_id': 'e2085be5-9137-4e4e-80b5-f1ffddc25423',
}


@pytest.mark.django_db
@pytest.mark.parametrize('event_serializer', [VALID_DATA], indirect=True)
def test_contains_expected_fields(event_serializer):
    event_serializer.is_valid()

    fields = ['name', 'category', 'data', 'timestamp', 'session_id']
    assert fields == list(event_serializer.data.keys())

    Session.objects.get(id=event_serializer.data['session_id']).delete()


@pytest.mark.django_db
@pytest.mark.parametrize('event_serializer', [VALID_DATA], indirect=True)
def test_create_valid_event(event_serializer):
    assert event_serializer.is_valid()

    with patch('events.serializers.create_event') as mocked_task:
        event_serializer.save()
        data = VALID_DATA.copy()
        mocked_task.delay.assert_called_with(data)

    Session.objects.get(id=data['session_id']).delete()


@pytest.mark.django_db
@pytest.mark.parametrize('event_serializer', [{}], indirect=True)
def test_invalid_data_serializer(event_serializer):
    assert event_serializer.is_valid() is False

    # assert that all fields have errors
    fields = ['name', 'category', 'data', 'timestamp', 'session_id']
    assert fields == list(event_serializer.errors.keys())

