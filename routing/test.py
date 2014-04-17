import unittest
from mvc.routing.route import Route

class RoutingTestFunctions(unittest.TestCase):
    def action (self, ignore):
        pass
    
    def action2 (self, ignore):
        pass
    
    def setUp(self):
        self.url = "/test"
        self.urladd = "/more"

    def test_action(self):
        self.assertTrue(callable(self.action))
        self.assertTrue(callable(self.action2))
    
    def test_route(self):
        route = Route(self.url, self.action)
        self.assertEqual(self.url, route.regex)
        self.assertEqual(self.action, route.target[-1])
    
    def test_route_empty(self):
        routing = Route()
        routing += Route('', self.action)
        (returned_action, context) = routing('')
        self.assertEqual(self.action, returned_action)
    
    def test_route_match(self):
        route = Route(self.url, self.action)
        (returned_action, context) = route(self.url)
        self.assertEqual(self.action, returned_action)

    def test_routing_single(self):
        routing = Route()
        routing += Route(self.url, self.action)
        (returned_action, context) = routing(self.url)
        self.assertEqual(self.action, returned_action)

    def test_routing_mutli(self):
        routing = Route()
        routing += Route(self.url, self.action)
        routing += Route(self.urladd, self.action2)
        (returned_action, context) = routing(self.url)
        self.assertEqual(self.action, returned_action)
        (returned_action, context) = routing(self.urladd)
        self.assertEqual(self.action2, returned_action)

    def test_routing_depth(self):
        routing = Route()
        child_routes = Route()
        routing += Route(self.url, child_routes)
        child_routes += Route(self.urladd, self.action)
        (returned_action, context) = routing(self.url + self.urladd)
        self.assertEqual(self.action, returned_action)

    def test_routing_organise(self):
        routing = Route()
        routing += Route(self.url, self.action)
        routing += Route(self.url + self.urladd, self.action2)
        
        (returned_action, context) = routing(self.url)
        self.assertEqual(self.action, returned_action)
        (returned_action, context) = routing(self.url + self.urladd)
        self.assertEqual(self.action2, returned_action)


if __name__ == '__main__':
    unittest.main()