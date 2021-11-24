from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from events.views import Events

urlpatterns = [
    re_path(r'^events/?$', Events.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
