from mvc.url.scheme import Scheme
from mvc.url.querystring import QueryString

class Url
    def __init__(self, host, path, query = None, scheme = "http", port = None):
        self.host = host
        self.path = path
        self.port = int(port)
        self.query = QueryString(query)
        self.scheme = Scheme[scheme]

    def __str__(self):
        url = self.url_scheme '://' + self.host
        if self.port != self.scheme.value:
            url += ':' + self.port
        url += self.path
        if self.query:
            url += '?' + self.query
        return url