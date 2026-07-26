import strawberry
from strawberry_django import type, input
from .models import Todo

@type(Todo)
class TodoType:
    id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: strawberry.auto

@input(Todo)
class TodoCreateInput:
    title: str
    description: str | None = None
    is_completed: bool = False

@input(Todo)
class TodoUpdateInput:
    id: strawberry.ID
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None

@input(Todo)
class TodoDeleteInput:
    id: strawberry.ID