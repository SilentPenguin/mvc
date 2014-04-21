from mvc.http.method import Method
import re
from urllib import parse

class Form(dict):
    def __init__(self, request = None):
        form_data = ''
        if request is not None:
            if request.method is Method.post:
                form_data = request.body
            if form_data and request.query_string:
                form_data = '&'.join((form_data, request.query_string))
            elif request.query_string:
                form_data = request.query_string
        super().__init__(parse.parse_qs(form_data))
    def __getattr__(self, name):
        return super().__getitem__(name)

    def __setattr__(self, name, value):
        super().__setitem__(name, value)

    def __str__(self):
        return '&'.join('{}={}'.format(k,v) for (k,vs) in sorted(super().items()) for v in sorted(vs))

class Model:
    def __init__(self, request = None):
        self.update(request)
    
    @property
    def valid(self):
        result = True
        public_attributes = [attribute for attribute in dir(self)
            if not attribute.startswith('_') and attribute is not 'valid']
        for attribute in public_attributes:
            try:
                result &= getattr(self,attribute).valid
            except:
                continue
        return result
    
    def update(self, request):
        self.form = Form(request)
        self._copy_form(self.form)
    
    def _copy_form(self, form_data):
        for name, item in form_data.items():
            self._assign_item(name, item)

    def _assign_item(self, name, item):
        if '.' in name:
            names = name.split('.')
            try:
                target = getattr(self, names[0])
            except:
                target = Model()
                setattr(self, names[0], target)
            target._assign_item(names[1:].join('.'), item)
        else:
            try:
                field = getattr(self, name)
                field.value = item
            except:
                field = Field()
                field.value = item
                setattr(self, name, field)

    def __getitem__(self, index):
        return getattr(self, index)

    def __contains__(self, index):
        return hasattr(self, index)

    def __contains__(self, index):
        return hasattr(self, index)

class Field:
    def __init__(self, default = None, validate = None, minimum = 0, maximum = 1):
        self.valid = False
        self.validate = validate
        self.minimum = minimum
        self.maximum = maximum
        self.value = default

    def __call__(self):
        return self.value
    
    @property
    def required(self):
        return self.minimum > 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        self._value = value
        self.valid = self.minimum <= len(value) <= self.maximum
        for item in value:
            if type(self.validate) is str:
                self.valid &= re.search(self.validate, item) is not None
            elif callable(self.validate):
                self.valid &= self.validate(item)
            else:
                break
