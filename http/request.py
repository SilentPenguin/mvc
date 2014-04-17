from .method import Method
from ..url.url import Url
from ..url.scheme import Scheme
from urllib import parse

class Request:
    def __init__(self, environment):
        
        '''
        Attributes:
            anything that appears in your wsgi implementation plus:
            host - http_host, or server_name if that is not defined
            url - a url object
        '''
    
        self.wsgi = {}
        self.html = {}
        self.request_method = Method['unrecognised']
        self.script_name = ''
        self.path_info = ''
        self.query_string = None
        self.content_type = None
        self.content_length = None
        self.server_port = 80
        self.server_name = None
        self.server_protocol = None
        self.url_scheme = 'http'
    
        self._environment = environment
    
        self._clone()
        self._pleasentaries()
        self._extras()

    #copy our environment across to the request as properties
    #it would have been nice if the wsgi spec required html with a dot
    def _clone(self):
        for name, value in self._environment.items():
            name = name.lower()
            if name.startswith('http-'):
                self.html[name[5:]] = value
            elif name.startswith('wsgi.'):
                self.wsgi[name[5:]] = value
            else:
                setattr(self, name, value)

    #make some of the present environment values more palletable
    def _pleasentaries(self):
        if 'request_method' in self and self.request_method is not None:
            self.request_method = Method(self.request_method)
        
        if 'content_length' in self and self.content_length is not None:
            try:
                self.content_length = int(self.content_length)
            except:
                self.content_length = 0

        if 'server_port' in self and self.server_port is not None:
            try:
                self.server_port = int(self.server_port)
            except:
                self.server_port = None

    #adds in some extra properties to save on some faff
    def _extras(self):
        path = parse.quote(self.script_name + self.path_info, '')
        host = self.http_host if 'http_host' in self else self.server_name
        self.url = Url(host, path, self.query_string, self.url_scheme, self.server_port)
        self.server_port = self.url.port

    def __getitem__(self, index):
        return getattr(self, index)

    def __contains__(self, index):
        return hasattr(self, index)
