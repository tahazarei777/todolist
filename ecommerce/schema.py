import strawberry
from strawberry.tools import merge_types
from to_do.mutations import TodoMutation,TodoQuery
from users.mutations import UserMutation,UsersQuery
RootQuery = merge_types("RootQuery", (TodoQuery, UsersQuery))
RootMutation = merge_types("RootMutation", (TodoMutation, UserMutation))

schema = strawberry.Schema(query=RootQuery, mutation=RootMutation)
