from rest_framework import serializers

from events.models import Event, Session
from events.tasks import create_event


class EventSerializer(serializers.ModelSerializer):
    session = serializers.UUIDField(required=True)
    data = serializers.DictField(required=True)

    class Meta:
        model = Event
        fields = ('name', 'category', 'data', 'timestamp')

    def __init__(self, app, *args, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        session = attrs.pop('session')
        try:
            Session.objects.get(id=session)
        except Session.DoesNotExist:
            Session.objects.create(id=session, app=self.app)

        attrs['session_id'] = session
        return attrs

    def create(self, validated_data):
        create_event.delay(validated_data)
