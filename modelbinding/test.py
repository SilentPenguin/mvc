import unittest
from mvc.modelbinding.models import Model, Field, Form
from mvc.http.request import Request
from mvc.http.method import Method

class ModelTestFunctions(unittest.TestCase):
    def test_empty_form(self):
        form = Form()

    def test_empty_model(self):
        model = Model()

    def test_post_form(self):
        request = Request()
        request.method = Method.post
        request.body = 'test=value'
        request.query_string = 'another=item'
        model = Model(request)
        self.assertEqual(model.form.test, ['value'])
        self.assertEqual(model.form.another, ['item'])

    def test_model_form(self):
        class MyModel(Model):
            test = Field()
        request = Request()
        request.method = Method.post
        request.body = 'test=value'
        model = Model(request)
        self.assertEqual(model.test.value, ['value'])
        self.assertEqual(model.test.valid, True)
        
    def test_model_form_valid(self):
        class MyModel(Model):
            test = Field(validate = '^value$')
        request = Request()
        request.method = Method.post
        request.body = 'test=value'
        model = MyModel(request)
        self.assertEqual(model.test.value, ['value'])
        self.assertEqual(model.test.validate, '^value$')
        self.assertEqual(model.test.valid, True)
        
    def test_model_form_invalid(self):
        class MyModel(Model):
            test = Field(validate = '^v$')
        request = Request()
        request.method = Method.post
        request.body = 'test=value'
        model = MyModel(request)
        self.assertEqual(model.test.value, ['value'])
        self.assertEqual(model.test.validate, '^v$')
        self.assertEqual(model.valid, False)

if __name__ == '__main__':
    unittest.main()