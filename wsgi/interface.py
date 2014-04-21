from mvc.http.response import Response
from mvc.http.request import Request
from mvc.controller.controller import Controller

class Interface:
    def __call__(self, environment, send_header):
        request = Request(environment)
        response = Response()

        result = self.route_map(request.url.path)
        print(request.url.path, result)
        if result is not None:
            (action, context) = result
            if action:
                controller = Controller(request)
                response = action(controller, **context)
        send_header(str(response.status.value) + ' ' + response.status.name, response.headers)
        return response