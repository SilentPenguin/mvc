from mvc.http.method import Method
    from mvc.http.query_string import QueryString
from urllib import quote

class Request ():
    
    DEFAULT_PORTS = {'http': 80, 'https': 443}
    
    environment = None
    wsgi = {}
    html = {}
    request_method = Method('unrecognised')
    script_name = ''
    path_info = ''
    query_string = ''
    content_type = ''
    content_length = 0
    server_name = ''
    server_port = ''
    server_protocol = ''
    
    path = ''
    host = ''
    secured = False

    def __init__(self, environment):
    
        self.environment = environment
    
        self._clone(environment)
        self._pleasentaries(environment)
        self._extras(environment)

    #copy our environment across to the request as properties
    #it would have been nice if the wsgi spec required html with a dot
    def _clone(self, environment)
        for name, value in environment.items():
            name = name.lower()
            if name.startswith('http-'):
                setattr(self.html, name[5:], value);
            else if name.startswith('wsgi.'):
                setattr(self.wsgi, name[5:], value);
            else:
                setattr(self, name, value);

    #make some of the present environment values more palletable
    def _pleasentaries(self, environment):
        if 'request_method' in self:
            self.request_method = Method(self.request_method.upper())
        
        if 'content_length' in self:
            self.content_length = int(self.content_length)

        if 'server_port' in self:
            self.server_port = int(self.server_port)

        if 'query_string' in self:
            self.query_string = QueryString(self.query_string)

    #adds in some extra properties to save on some faff
    def _extras(self, environment):
        self.path = quote(self.script_name + self.path_info, '')
        self.host = self.http_host if 'http_host' in self else self.server_name
        self.secured = self.wsgi.url_scheme in SECURE_PROTOCOLS
        self.address = self._construct_address();
    
    def _construct_address(self):
        url = self.wsgi.url_scheme '://' + self.host
        if self.url_scheme in DEFAULT_PORTS \
                and self.server_port != DEFAULT_PORTS[self.url_scheme]:
            url += ':' + self.server_port
        url += self.path
        if 'query_string' in self:
            url += '?' + self.query_string

    def __getitem__(self, index):
        return getattr(self,index)

    def __contains__(self, index):
        return index in self.environment or hasattr(self, index)
