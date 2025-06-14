class EmptyDescriptionException(Exception):
    def __init__(self, message: str):
        self.message = f"Description at with content:<{message}> is invalid. It is empty."
        super().__init__(self.message)

class EmptyCompleteDateException(Exception):
    def __init__(self, message: str):
        self.message = f"Completed at with content:<{message}> is invalid. It is empty."
        super().__init__(self.message)

class InvalidCompleteDateException(Exception):
    def __init__(self, message: str):
        self.message = f"{message} is invalid. It is earlier than the day of creation."
        super().__init__(self.message)


class EmptyTitleException(Exception):
    def __init__(self, message: str):
        self.message = f"Title with content:<{message}> is invalid. It is empty."
        super().__init__(self.message)
