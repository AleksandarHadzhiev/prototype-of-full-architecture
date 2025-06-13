import asyncio

class CreateTodoValidation():
    def __init__(self, data: dict):
        self.data:dict = data
        self.errors = []

    async def _check_for_expected_keys(self):
        if "title" not in self.data:
            self.errors.append("Title is missing")
        else:
            for key in list(self.data.keys()):
                self._check_if_field_is_empty_string(key)

    async def _check_if_field_is_empty_string(self, field: str):
        if self.data[field].strip() == "":
            self.errors.append(f"{field} is empty")
    async def validate_data(self):
        asyncio.gather(self._check_for_expected_keys(), self._check_if_field_is_empty_string())