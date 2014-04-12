from enum import Enum, unique

@unique
class Method(Enum):
    """Various http method verbs"""
    
    get = "GET"
    head = "HEAD"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    trace = "TRACE"
    options = "OPTIONS"
    connect = "CONNECT"
    patch = "PATCH"

    unrecognised = None

    __str__(self):
        return self.value