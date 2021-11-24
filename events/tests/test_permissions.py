import pytest

from events.permissions import IsValidApplication


@pytest.mark.django_db
def test_invalid_permission_application_token(mocked_request):
    validor = IsValidApplication()
    assert validor.has_permission(mocked_request, None) is False


@pytest.mark.django_db
def test_valid_permission_application_token(mocked_request, new_application):
    mocked_request.META['HTTP_AUTHORIZATION'] = new_application.token
    validor = IsValidApplication()
    assert validor.has_permission(mocked_request, None)

    new_application.delete()
