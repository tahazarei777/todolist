import strawberry
import strawberry_django
from django.contrib.auth import authenticate

from .jwt import create_access_token
from .models import User
from .types import UserType

@strawberry.type
class LoginResponse:
    access_token: str
    username: str
    email: str


@strawberry.type
class RegisterResponse:
    access_token: str
    username: str
    email: str


@strawberry.type()
class UsersQuery:
    users: list[UserType] =strawberry_django.field()
    user : UserType | None= strawberry_django.field()




@strawberry.type
class UserMutation:

    @strawberry.mutation()
    def login(
            self,
            username: str,
            password: str,
    ) -> LoginResponse:

        user = authenticate(
            username=username,
            password=password,
        )

        if user is None:
            raise Exception("Invalid username or password")

        token = create_access_token(user)

        return LoginResponse(
            access_token=token,
            username=user.username,
            email=user.email,
        )

    @strawberry.mutation(
        description="Create a new user"
    )
    def register(
            self,
            username: str,
            email: str,
            password: str,
    ) -> RegisterResponse:

        if User.objects.filter(username=username).exists():
            raise Exception("Username already exists")

        if User.objects.filter(email=email).exists():
            raise Exception("Email already exists")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        token = create_access_token(user)

        return RegisterResponse(
            access_token=token,
            username=user.username,
            email=user.email,
        )
