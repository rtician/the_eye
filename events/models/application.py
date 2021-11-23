from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        app_label = 'events'
        db_table = 'session'
