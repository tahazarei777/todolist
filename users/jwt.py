import jwt

from datetime import timedelta

from django.conf import settings
from django.utils import timezone


def create_access_token(user):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": timezone.now() + timedelta(
            seconds=settings.JWT_ACCESS_TOKEN_LIFETIME
        ),
        "iat": timezone.now(),
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )