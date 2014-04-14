from http.response import Response
from http.statuscode import StatusCode
class Controller:
    '''
    The base class for useful controller functions
    '''
    def __init__(self, template_engines):
        self._template_engines = template_engines

    def view(self, model = None):
        for template_engine in self.template_engines:
            body = template_engine(model)
            if body is not None:
                return Response(StatusCode.ok, body)

    def not_found(self):
        return Response(StatusCode.not_found)