from mvc.http import StatusCode

class Response:
    __init__(self, status = StatusCode.not_found):
        self.status = status

    __iter__(self):
        pass