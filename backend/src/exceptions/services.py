class InvalidRequestException(Exception):
    def __init__(self, detail: str = "Invalid request"):
        super().__init__(detail)


class NoRightsException(Exception):
    def __init__(self, detail: str = "No access rights"):
        super().__init__(detail)


class NotFoundException(Exception):
    def __init__(self, detail: str = "Not found"):
        super().__init__(detail)


class ServerError(Exception):
    def __init__(self, detail: str = "Internal server error"):
        super().__init__(detail)
