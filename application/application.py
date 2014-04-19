from ..routing.route import Route
from ..wsgi.interface import Interface
from wsgiref.simple_server import make_server


class Application(Interface):
    route_map = Route()
    def __init__ (self, run_server = False):
        super().__init__()
        if run_server:
            server = TestServer(self)

class TestServer:
    def __init__ (self, interface, port=8000):
        self.server = make_server('localhost', port, interface)
        self.server.serve_forever()