from unittest import TestCase
from http.request import Request

class RequestTestFunctions(TestCase):
    def test_empty_request(self):
        request = Request({})

    def test_in_request(self):
        request = Request({'key':'value'})
        self.assertTrue('key' in request)
        self.assertFalse('notkey' in request)
        self.assertEqual(request['key'],'value')



if __name__ == '__main__':
    unittest.main()