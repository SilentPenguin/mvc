from mvc.http.method import Method

class Request ():
    
    request_method = Method("unrecognised")
    script_name = ""
    path_info = ""
    query_string = ""
    content_type = ""
    content_length = 0
    server_name = ""
    server_port = ""
    server_protocol = ""

    def __init__(self, environment):
    
        #copy our environment across to the request attributes
        for name, value in environment.items():
            setattr(self, name.lower(), value);

        #make some of the present environment values more palletable
        if "REQUEST_METHOD" in environment:
            self.request_method = Method(self.request_method)
        if "CONTENT_LENGTH" in environment:
            self.content_length = int(self.content_length)