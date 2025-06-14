from datetime import datetime
from pydantic import BaseModel, field_validator
from src.exceptions.create_todo_exceptions import InvalidCompleteDateException, EmptyTitleException, EmptyCompleteDateException, EmptyContentException

class CreateTodo(BaseModel):
    title: str
    content: str | None = None
    date_to_complete: str | None = None

    @field_validator("title")
    def title_not_empty(cls, title: str):
        if title.strip().replace(" ", "") == "":
            raise EmptyTitleException(message=title.strip().replace(" ", ""))
        return title       

    @field_validator("content")
    def description_not_empty(cls, content: str):
        if content != None and content.strip().replace(" ", "") == "":
            raise EmptyContentException(message=content.strip().replace(" ", ""))
        return content

    @field_validator("date_to_complete")
    def compare_completed_at_with_created_at(cls, date_to_complete: str):
        if date_to_complete != None and date_to_complete.strip().replace(" ", "") == "":
           raise EmptyCompleteDateException(date_to_complete)
        else:
            completed_at_as_date = datetime.strptime(date_to_complete, '%m/%d/%y %H:%M:%S')
            current_date = datetime.now()

            difference = completed_at_as_date - current_date
            if (difference.total_seconds() < 0):
                raise InvalidCompleteDateException(message=date_to_complete)
            return date_to_complete
