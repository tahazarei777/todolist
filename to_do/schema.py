import strawberry

from .mutations import TodoQuery, TodoMutation

todo_schema = strawberry.Schema(query=TodoQuery, mutation=TodoMutation)
