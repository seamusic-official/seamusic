class NoRightsException(Exception):
    def __init__(self, detail: str = "No access rights"):
        super().__init__(detail)


class NotFoundException(Exception):
    def __init__(self, detail: str = "Not found"):
        super().__init__(detail)
