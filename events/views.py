from rest_framework import status, views

from events.models import Application
from events.serializers import EventSerializer
from events.responses import ErrorResponse, SuccessResponse


class Events(views.APIView):
    def post(self, request):
        app = Application.objects.get(token=request.META['HTTP_AUTHORIZATION'])
        data = request.data.copy()

        serializer = EventSerializer(data=data, app=app)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse()

        return ErrorResponse(serializer.errors)
