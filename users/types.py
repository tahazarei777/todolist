import strawberry_django
from strawberry import *

from .models import User, Profile


@strawberry_django.type(User)
class UserType:
    first_name: auto
    last_name: auto
    email: auto
    username: auto
    password: auto
    phone: auto
    address: auto
    role: auto
    is_active: auto
    date_joined: auto


@strawberry_django.input(User, partial=True)
class UserInput:
    first_name: auto = None
    last_name: auto = None
    email: auto = None
    username: auto = None
    password: auto = None


@strawberry_django.type(Profile)
class ProfileType:
    user: auto
    avatar: auto


@strawberry_django.input(Profile, partial=True)
class ProfileInput:
    avatar: auto
