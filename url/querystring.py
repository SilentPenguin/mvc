from urllib import parse
class QueryString(dict):
    def __init__(self, query_string):
        super().__init__(parse.parse_qs(query_string))

    def __str__(self):
        return '&'.join('{}={}'.format(k,v) for (k,vs) in sorted(super().items()) for v in vs)
