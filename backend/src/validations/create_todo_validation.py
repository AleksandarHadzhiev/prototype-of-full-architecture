from datetime import datetime
from pydantic import BaseModel, field_validator
from src.exceptions.create_todo_exceptions import InvalidCompleteDateException, EmptyTitleException, EmptyCompleteDateException, EmptyDescriptionException

class CreateTodo(BaseModel):
    title: str
    description: str | None = None
    completed_at: str | None = None

    @field_validator("title")
    def title_not_empty(cls, title: str):
        if title.strip().replace(" ", "") == "":
            raise EmptyTitleException(message=title.strip().replace(" ", ""))

    @field_validator("description")
    def title_not_empty(cls, description: str):
        if description != None and description.strip().replace(" ", "") == "":
            raise EmptyDescriptionException(message=description.strip().replace(" ", ""))

    @field_validator("completed_at")
    def compare_completed_at_with_created_at(cls, completed_at: str):
        if completed_at != None and completed_at.strip().replace(" ", "") == "":
           raise EmptyCompleteDateException(completed_at)
        else:
            completed_at_as_date = datetime.strptime(completed_at, '%m/%d/%y %H:%M:%S')
            current_date = datetime.now()

            difference = completed_at_as_date - current_date
            if (difference.total_seconds() < 0):
                raise InvalidCompleteDateException(message=completed_at)
