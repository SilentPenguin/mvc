from mvc.http.response import Response
from mvc.http.request import Request
from mvc.routing.route import route_map
from mvc.controller.controller import Controller
from wsgiref.simple_server import make_server

class Interface:
    def __init__(self):
        self.route_map = route_map

    def __call__(self, environment, send_header):
        request = Request(environment)

        response = Response()

        result = self.route_map(request.url.path)
        print(request.url.path, result)
        if result is not None:
            (controller, context) = result
            if controller:
                response = controller(Controller(), **context)
        send_header(str(response.status.value) + ' ' + response.status.name, response.headers)
        return response

class TestServer:
    def __init__ (self, interface, port=8000):
        self.server = make_server('localhost', port, interface)
        self.server.serve_forever()