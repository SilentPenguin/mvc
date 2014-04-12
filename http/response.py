from mvc.http.statuscode import StatusCode

class Response:

    status = StatusCode.not_found
    
    body = ""
    
    @property
    response_length(self):
        return len(response_body)

    __init__(self, status = StatusCode.not_found):
        self.status = status

    __next__(self):
        pass