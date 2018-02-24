class MalformedTokenException(Exception):
    def __init__(self, message) -> None:
        super().__init__("Malformed token: " + message)
