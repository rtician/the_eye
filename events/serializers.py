from rest_framework import serializers

from events.models import Event, Session
from events.tasks import create_event


class EventSerializer(serializers.ModelSerializer):
    session_id = serializers.UUIDField(required=True)
    data = serializers.DictField(required=True)

    class Meta:
        model = Event
        fields = ('name', 'category', 'data', 'timestamp', 'session_id')

    def __init__(self, *args, **kwargs):
        self.app = kwargs.pop('app')
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        session = attrs['session_id']
        try:
            Session.objects.get(id=session)
        except Session.DoesNotExist:
            Session.objects.create(id=session, app=self.app)

        return attrs

    def create(self, validated_data):
        event = Event(**validated_data)

        json_data = {
            'name': event.name,
            'category': event.category,
            'data': event.data,
            'timestamp': str(event.timestamp),
            'session_id': str(event.session.id),
        }
        create_event.delay(json_data)

        return event
