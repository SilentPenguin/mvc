from unittest import TestCase
from routing.route import Route

class RoutingTestFunctions(TestCase):
    def action (self, ignore):
        pass
    
    def setUp(self):
        self.url = "/test"
        self.urladd = "/more"

    def test_action(self):
        self.assertTrue(callable(self.action))
    
    def test_route(self):
        route = Route(self.action, self.url)
        self.assertEqual(self.url, route.regex)
        self.assertEqual(self.action, route.target[-1])
    
    def test_route_match(self):
        route = Route(self.action, self.url)
        returned_action = route(self.url)
        self.assertEqual(self.action, returned_action)

    def test_routing_single(self):
        routing = Route()
        routing += Route(self.action, self.url)
        returned_action = routing(self.url)
        self.assertEqual(self.action, returned_action)

    def test_routing_depth(self):
        routing = Route()
        child_routes = Route()
        routing += Route(child_routes, self.url)
        child_routes += Route(self.action, self.urladd)
        returned_action = routing(self.url + self.urladd)
        self.assertEqual(self.action, returned_action)

if __name__ == '__main__':
    unittest.main()