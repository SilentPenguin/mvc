from http.statuscode import StatusCode

class Response:
    
    @property
    response_length(self):
        return len(response_body)

    __init__(self, status = StatusCode.not_found, body = ''):
        self.status = status
        self.body = body

    __next__(self):
        return self.body