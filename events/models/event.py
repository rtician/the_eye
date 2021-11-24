from django.db import models


class Event(models.Model):
    session = models.ForeignKey('events.Session', on_delete=models.RESTRICT)

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField()

    class Meta:
        app_label = 'events'
        db_table = 'event'
        ordering = ('-timestamp',)
        indexes = (
            models.Index(fields=['timestamp'], name='timestamp_idx'),
        )
