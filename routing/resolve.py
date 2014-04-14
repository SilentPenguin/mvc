class Resolve:

    '''
    what the routing finds as a solution.
    attributes - what to pass to the controller as arguments
    controller - the object to call
    '''

    def __init__(self):
        self.attributes = {}
        self.controller = None
    
    def __call__(self, *args, **kwargs):
        return self.controller(*args, **kwargs)