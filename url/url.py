from mvc.url.scheme import Scheme
from mvc.url.querystring import QueryString

from urllib.parse import unquote

class Url:
    def __init__(self, host, path, query = None, scheme = 'http', port = None):
        self.host = host
        self.path = unquote(path)
        self.scheme = Scheme[scheme]
        self.port = int(port) if port is not None else self.scheme.value
        self.query = QueryString(query)

    def __str__(self):
        url = self.scheme.name + '://' + self.host
        if self.port != self.scheme.value:
            url += ':' + str(self.port)
        url += self.path
        if self.query:
            url += '?' + str(self.query)
        return url