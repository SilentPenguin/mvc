from .statuscode import StatusCode

class Response:
    
    @property
    def response_length(self):
        return len(response_body)

    def __init__(self, status = StatusCode.not_found, body = ''):
        self.status = status
        self.body = body
        self.headers = []

    def __iter__(self):
        return iter([self.body.encode("utf-8")])