import re

class Route:
    '''
    The Route class is a conditional tree node.
    If the regex matches it carries on looking down the route tree looking
    for callables.
    When the tree reaches a callable that isn't itself, it returns it, otherwise
    a call will return None.
    
    Attributes:
        regex(str) - the condition this callable must meet in order to access
            the target children
        target(list of callables) - child callables to resolve
        default(dict) - currently unused
        raw (bool) - uses the regex raw, rather than appending nicities
    '''
    def __init__(self, target = None, regex = None, default = None, raw = False):
        '''
        Note:
            use this without any arguments if you intend to use += at some point
            after
        Args:
            target (callable): nodes to add, either more Routes, or another 
                callable
            regex (string): the condition this callable must meet in order to 
                access target children
            default(dict) - currently unused
        '''
        self.regex = regex
        self.raw = raw
        self.target = []
        self.default = default
        if target:
            self += target

    def __call__(self, test, _resolve = None):
        return self.resolve(test, _resolve)
    
    def resolve(self, test, _resolve = None):
        '''
        Where the routing actually happens, if the regex attribute is not empty
        it will be checked to see if the test string matches, if it does.
        that bit of the test string will be removed.
        
        Args:
            test (str): string to test
        '''
        matches = True
        if self.regex:
            matches = re.search(('^' if not self.raw else '') + self.regex, test)
        if matches:
            childtest = test
            
            if self.regex:
                childtest = re.sub(self.regex, '', test, count = 1)
                if _resolve is None:
                    _resolve = {}
                _resolve.update(matches.groupdict())
        
            if self.default:
                _resolve.update(self.default)
            
            for item in self.target:
                if issubclass(item.__class__, self.__class__):
                    result = item(childtest, _resolve)
                    if result:
                        return result
                else:
                    return (item, _resolve)
    
    __call__.__doc__ = resolve.__doc__

    def __iadd__(self, callable):
        '''
        my_route += Route("$blah", my_callable)
        my_route += my_controller
        '''
        try:
            self.target.extend(callable)
        except:
            self.target.append(callable)
        return self

    def __isub__(self, callable):
        '''
        my_route -= my_controller
        '''
        self.target.remove(callable)
        return self
