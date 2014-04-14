from http.method import Method
from url.url import Url
from urllib import quote

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
        self.request_method = Method('unrecognised')
        self.script_name = ''
        self.path_info = ''
        self.query_string = ''
        self.content_type = ''
        self.content_length = 0
        self.server_name = ''
        self.server_port = ''
        self.server_protocol = ''
    
        self._environment = environment
    
        self._clone()
        self._pleasentaries()
        self._extras()

    #copy our environment across to the request as properties
    #it would have been nice if the wsgi spec required html with a dot
    def _clone(self)
        for name, value in self._environment.items():
            name = name.lower()
            if name.startswith('http-'):
                setattr(self.html, name[5:], value);
            else if name.startswith('wsgi.'):
                setattr(self.wsgi, name[5:], value);
            else:
                setattr(self, name, value);

    #make some of the present environment values more palletable
    def _pleasentaries(self):
        if 'request_method' in self:
            self.request_method = Method(self.request_method.upper())
        
        if 'content_length' in self:
            self.content_length = int(self.content_length)

        if 'server_port' in self:
            self.server_port = int(self.server_port)

    #adds in some extra properties to save on some faff
    def _extras(self):
        path = quote(self.script_name + self.path_info, '')
        host = self.http_host if 'http_host' in self else self.server_name
        self.url = Url(host, path, query_string, self.url_scheme, self.server_port)    

    def __getitem__(self, index):
        return getattr(self,index)

    def __contains__(self, index):
        return index in self.environment or hasattr(self, index)
