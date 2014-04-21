from mvc.routing.route import Route
from mvc.wsgi.interface import Interface
from mvc.application.testserver import TestServer

class Application(Interface):
    route_map = Route()
    def __init__ (self, run_server = False):
        super().__init__()
        if run_server:
            server = TestServer(self)