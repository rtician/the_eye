import json

import pytest


@pytest.mark.django_db
def test_success_creating_events(client, session,):
    data = {
        'session_id': str(session.id),
        'name': 'pageview',
        'category': 'page interaction',
        'data': {
            'host': 'www.consumeraffairs.com',
            'path': '/',
        },
        'timestamp': '2021-01-01 09:15:27.243860',
    }
    client.credentials(HTTP_AUTHORIZATION=session.app.token)
    response = client.post(
        '/api/events',
        data=json.dumps(data),
        content_type='application/json',
    )
    assert 204 == response.status_code


@pytest.mark.django_db
def test_invalid_request(client, application):
    client.credentials(HTTP_AUTHORIZATION=application.token)
    response = client.post(
        '/api/events',
        data=json.dumps({}),
        content_type='application/json',
    )
    assert 400 == response.status_code


@pytest.mark.django_db
def test_invalid_application(client):
    response = client.post(
        '/api/events',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert 403 == response.status_code
