class QueryString:
    _raw_string = ''
    values = {}
    __init__(self, query_string):
        self._raw_string = query_string
        fields = query_string.split('&')
        for field in fields:
            result = field.split('=')
            if len(result) == 2:
                values[result[0]] = result[1]

    __str__(self):
        return _raw_string
