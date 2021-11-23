from django.db import models


class Session(models.Model):
    id = models.UUIDField(primary_key=True)
    app = models.ForeignKey('events.Application', on_delete=models.RESTRICT)

    class Meta:
        app_label = 'events'
        db_table = 'session'
