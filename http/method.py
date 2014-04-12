from enum import Enum

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