from mvc.http.response import Response
from mvc.http.statuscode import StatusCode
from mvc.templating.template import TemplateEngine

class Controller:
    '''
    The base class for useful controller functions
    '''
    def __init__(self, request = None):
        self._request = request
        self._template_engine = TemplateEngine

    def view(self, model = None, template=''):
        compiled_template = self._template_engine(template)
        body = compiled_template(model)
        return Response(StatusCode.ok, body)

    def not_found(self):
        return Response(StatusCode.not_found)

    def __call__(self, action, **kwargs):
        return getattr(self, action)(**kwargs)