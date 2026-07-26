import strawberry
import strawberry_django
from strawberry_django import mutations
from .types import TodoType, TodoCreateInput, TodoUpdateInput, TodoDeleteInput
from .models import Todo


@strawberry.type()
class TodoQuery:
    todos: list[TodoType] = strawberry_django.field()

    @strawberry_django.field()
    def todo(self, id: int) -> TodoType | None:
        return Todo.objects.filter(id=id).first()


@strawberry.type()
class TodoMutation:
    create_todo: TodoType = mutations.create(TodoCreateInput)
    update_todo: TodoType = mutations.update(TodoUpdateInput, argument_name="data")
    delete_todo: TodoType = mutations.delete(TodoDeleteInput, argument_name="data")