from ..http.response import Response
from ..http.statuscode import StatusCode
from ..templating.template import TemplateEngine

class Controller:
    '''
    The base class for useful controller functions
    '''
    def __init__(self):
        self._template_engine = TemplateEngine

    def view(self, model = None, template=''):
        compiled_template = self._template_engine(template)
        body = compiled_template(model)
        return Response(StatusCode.ok, body)

    def not_found(self):
        return Response(StatusCode.not_found)

    def __call__(self, action, **kwargs):
        return getattr(self, action)(**kwargs)