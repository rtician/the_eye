import uuid

from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=500)
    token = models.CharField(max_length=64, unique=True)

    class Meta:
        app_label = 'events'
        db_table = 'application'

    def unique_token_generator(self):
        token = uuid.uuid4()

        cls = self.__class__
        if cls.objects.filter(token=token).exists():
            return self.unique_token_generator()
        return token

    def save(self, **kwargs):
        if not self.token:
            self.token = self.unique_token_generator()
        super(Application, self).save(**kwargs)
