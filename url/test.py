from unittest import TestCase
from url.url import Url

class urlTestFunctions(TestCase):
    
    def setUp(self):
        self.host = 'example.com'
        self.path = '/test/path'
        self.query = 'another=field&test=value'
        self.port = 43
        self.scheme = 'https'

    def test_basic_url(self):
        url = Url(self.host, self.path)
        self.assertEqual('http://' + self.host + self.path, url.__str__())

    def test_querystring_url(self):
        url = Url(self.host, self.path, query = self.query)
        self.assertEqual('http://' + self.host + self.path + '?' + self.query,
            url.__str__())
            
    def test_scheme_url(self):
        url = Url(self.host, self.path, scheme = self.scheme)
        self.assertEqual(self.scheme + '://' + self.host + self.path,
            url.__str__())

    def test_port_url(self):
        url = Url(self.host, self.path, port = self.port)
        self.assertEqual('http://' + self.host +':' + str(self.port) +
            self.path, url.__str__())

    def test_everything_url(self):
        url = Url(self.host, self.path, port = self.port,
            query = self.query, scheme = self.scheme)
        self.assertEqual(self.scheme + '://' + self.host +':' + str(self.port)
            + self.path + '?' + self.query, url.__str__())

if __name__ == '__main__':
    unittest.main()