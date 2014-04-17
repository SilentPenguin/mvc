from mvc.http.response import Response
from mvc.http.statuscode import StatusCode

class Controller:
    '''
    The base class for useful controller functions
    '''
    def __init__(self, template_engine):
        self._template_engine = template_engine

    def view(self, model = None, template=''):
        compiled_template = template_engine(template)
        body = compiled_template(model)
        return Response(StatusCode.ok, body)

    def not_found(self):
        return Response(StatusCode.not_found)