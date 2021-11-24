from rest_framework import response, status


class JsonResponse(response.Response):
    def __init__(self, *args, **kwargs):
        kwargs.pop('content_type', None)
        super().__init__(content_type='application/json', *args, **kwargs)


class ErrorResponse(JsonResponse):
    def __init__(self, data, *args, **kwargs):
        kwargs.pop('data', None)
        kwargs.pop('status', None)

        data = {
            'error': True,
            'data': data
        }
        super().__init__(data=data, status=status.HTTP_400_BAD_REQUEST, *args, **kwargs)


class SuccessResponse(JsonResponse):
    def __init__(self, *args, **kwargs):
        kwargs.pop('status', None)
        super().__init__(status=status.HTTP_204_NO_CONTENT, *args, **kwargs)
