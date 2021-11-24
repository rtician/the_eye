from events.responses import ErrorResponse, JsonResponse, SuccessResponse


def test_json_response():
    response = JsonResponse()
    assert 200 == response.status_code
    assert 'application/json' == response.content_type

    # assert that the content-type doesn't change
    response = JsonResponse(status=201, content_type='image/jpg')
    assert 201 == response.status_code
    assert 'application/json' == response.content_type


def test_error_response():
    response = ErrorResponse([])
    assert 'error' in response.data
    assert 'data' in response.data
    assert 400 == response.status_code

    # assert that the HTTP code doesn't change
    response = ErrorResponse([], status=200)
    assert 400 == response.status_code

    # assert that the error msg is correctly added
    data = [{'foo': 'bar'}]
    response = ErrorResponse(data)
    assert data == response.data['data']


def test_success_response():
    response = SuccessResponse([])
    assert 204 == response.status_code

    # assert that the HTTP code doesn't change
    response = SuccessResponse([], status=400)
    assert 204 == response.status_code
