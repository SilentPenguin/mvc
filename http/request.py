from mvc.http import Method

class Request ():
    
    request_method = None
    script_name = None
    path_info = None
    query_string = None
    content_type = None
    content_length = None
    server_name = None
    server_port = None
    server_protocol = None

    def __init__(self, environment):
    
        #copy our environment across to the request attributes
        for name, value in environment.items():
            setattr(self, name.lower(), value);

        #make some of the present environment values more palletable
        self.request_method = Method(self.request_method)
        self.content_length = int(self.content_length)