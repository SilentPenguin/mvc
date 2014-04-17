import unittest
from .template import TemplateEngine

class Model:
    value = None

class TemplateTestFunctions(unittest.TestCase):
    def test_template_engine(self):
        template = TemplateEngine('./templating/example.pyhtml',
                override_compile_cache = True)
        code = template(Model)
        with open('./templating/example.html', 'r') as f:
            example_code = f.read()
            self.assertEqual(code, example_code)

if __name__ == '__main__':
    unittest.main()