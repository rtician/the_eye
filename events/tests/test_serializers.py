from datetime import datetime
from unittest.mock import patch
from uuid import UUID

import pytest

VALID_DATA = {
    'name': 'foo',
    'category': 'foo',
    'data': {},
    'timestamp': '2021-01-01 09:15:27.243860',
    'session': 'e2085be5-9137-4e4e-80b5-f1ffddc25423',
}


@pytest.mark.django_db
@pytest.mark.parametrize('event_serializer', [VALID_DATA], indirect=True)
def test_contains_expected_fields(event_serializer):
    event_serializer.is_valid()

    fields = ['name', 'category', 'data', 'timestamp', 'session']
    assert fields == list(event_serializer.data.keys())


@pytest.mark.django_db
@pytest.mark.parametrize('event_serializer', [VALID_DATA], indirect=True)
def test_create_valid_event(event_serializer):
    assert event_serializer.is_valid()

    with patch('events.serializers.create_event') as mocked_task:
        event_serializer.save()
        data = VALID_DATA.copy()
        data['timestamp'] = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        data['session_id'] = UUID(data.pop('session'))
        mocked_task.delay.assert_called_with(data)


@pytest.mark.django_db
@pytest.mark.parametrize('event_serializer', [{}], indirect=True)
def test_invalid_data_serializer(event_serializer):
    assert event_serializer.is_valid() is False

    # assert that all fields have errors
    fields = ['name', 'category', 'data', 'timestamp', 'session']
    assert fields == list(event_serializer.errors.keys())

