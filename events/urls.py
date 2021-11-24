from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from events.views import Events

urlpatterns = [
    url(r'^events/?$', Events.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
