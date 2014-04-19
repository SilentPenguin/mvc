import re
from itertools import takewhile

class Route:
    '''
    The Route class is a radix tree, which will return a specific value based on
    regex matching.
    
    The tree will optimise itself when calling += so if there are two
    routes with branching regex, the point where the regex differs will be split
    off into two new Route objects.
    
    this means you can, if you want, select a specific route to add your Route
    to, and it will work, or you can add it to the top, and the tree will be
    followed down to the point where your tree differs, both will produce the 
    same result, so there's no advantage to using the djangoish include() syntax 
    by setting your route target to some child urls, unless that's how you 
    choose to live your life.
    
    this means several styles of syntax are possible:
        flask style @route(url) where route acts on the route table for you
        django style Route('url', target) where you handcraft your structure
        asp.net mvc style route_table += Route('url', target)
    
    it should be possible to use these together without issues, although you
    should probably pick which to use.
    
    Being an avid django and asp.net mvc user, I honestly think the django 
    routing style above demonstrates the least merit since it binds all your 
    urls together on the application side
    
    However, they all have their advantages and disadvantages:
        flask, routing is directly on the code, so it's closest to where it's
        used, but it's also extra noise which isn't really helping.
        django, routing can be modularised to save on url typing with less faff, 
        it's harder to ensure each part of your website is entirely independent.
        asp.net, much the same as flask, except you can keep your code seperate
    '''
    
    def __init__(self, regex = '', target = None, default = None):
        self.regex = regex
        self.target = []
        self.default = default if default is not None else {}
        self += target

    def __call__(self, test, _regex = ''):
        return self.resolve(test, _regex)
    
    def resolve(self, test, _regex = ''):
        '''
        takes in a test string, and finds an exact match in the tree
        
        Args:
            test(str) - a string to test radix tree against
        
        Note:
            resolve always returns the most qualified route meaning a test
            string '/my/string' won't return at the node '/my'
        '''
        _regex += self.regex
        for target in self.target:
            if issubclass(target.__class__, self.__class__):
                result = target(test, _regex)
                if result is not None:
                    return result
            else:
                matches = re.search('^' + _regex + '$', test)
                if matches:
                    return (target, matches.groupdict())
                else:
                    break
    
    __call__.__doc__ = resolve.__doc__

    def __iadd__(self, other):
        if issubclass(other.__class__, self.__class__):
            for route in self.target:
                regex = zip(route.regex, other.regex)
                similar = ''.join(x for (x, y) in takewhile(lambda x: x[0] == x[1], regex))
                if similar:
                    base_route = Route(route.regex[:len(similar)])
                    other.regex = other.regex[len(similar):]
                    route.regex = route.regex[len(similar):]
                    base_route += other
                    base_route += route
                    self.target = [base_route]
                    return self
    
        if other is not None:
            self.target.append(other)

        return self
    def __isub__(self, other):
        raise NotImplementedError

from ..application.application import Application
def route(target, regex, default = None):
    '''
    Decorator which handles adding routes. Just stick these on your callables
    and the route_table will be populated for you.
    
    Args:
        same as Route,
    '''
    
    Application.route_map += Route(regex, target, default)

    return f
        