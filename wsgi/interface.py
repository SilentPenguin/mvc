from mvc.http.response import Response
from mvc.http.request import Request

class interface:
    def __init__(self, routemap):
        self.routemap

    def __call__(self, environment, send_header):
        request = Request(environment)

        response = Response()

        (controller, context) = self.routemap(request.url)
        
        if controller:
            response = controller(**context)

        send_header(response.status.value, response.headers)
        yeild response