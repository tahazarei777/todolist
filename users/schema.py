import strawberry

from .mutations import UserMutation, UsersQuery

users_schema = strawberry.Schema(
    query=UsersQuery,
    mutation=UserMutation,
)
