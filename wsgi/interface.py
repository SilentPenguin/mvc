from http.response import Response
from http.request import Request

class interface:
    def __init__(self, routemap):
        self.routemap

    def __call__(self, environment, send_header):
        request = Request(environment)

        response = Response()

        controller = self.routemap(request.url)
        
        if callable(controller):
            response = controller()

        send_header(response.status.value, response.headers)
        yeild response