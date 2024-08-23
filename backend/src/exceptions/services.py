class InvalidRequestException(Exception):
    def __init__(self, detail: str = "Invalid request"):
        self.detail = detail
        super().__init__(detail)


class NoRightsException(Exception):
    def __init__(self, detail: str = "No access rights"):
        self.detail = detail
        super().__init__(detail)


class NotFoundException(Exception):
    def __init__(self, detail: str = "Not found"):
        self.detail = detail
        super().__init__(detail)


class ServerError(Exception):
    def __init__(self, detail: str = "Internal server error"):
        self.detail = detail
        super().__init__(detail)
