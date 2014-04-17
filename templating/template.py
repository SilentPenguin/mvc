import re
import keyword
import os.path
import importlib.machinery

class TemplateEngine:
    def __init__(self, template_path, _override_compile_cache = False):
        self.template_path = template_path
        self.file_name = self.template_path.rsplit('.', 1)[0] + '.py'
        self.base = TemplateNode()
        self.base.level = -1
        self.tab_size = 4
        if self._check_to_compile() or _override_compile_cache:
            self.code = self._compile_template()
            self._write_template_code()
    
    def _check_to_compile(self):
        try:
            return os.path.getmtime(self.template_path) \
                > os.path.getmtime(self.file_name)
        except:
            return True
    
    def _compile_template(self):
        with open(self.template_path, 'r') as f:
            for line in f.readlines():
                if line:
                    node = TemplateNode(line, self.tab_size)
                    self.base += node
        return self.base.compile_node()

    def _write_template_code(self):
        with open(self.file_name, 'w+') as f:
            f.write('def view_code(view, model, _result=""):\n')
            code = ('    ' + line + '\n' for line in self.code.split('\n'))
            f.writelines(code)
            f.write('    return _result')
    
    def __call__(self, model):
        loader = importlib.machinery.SourceFileLoader("module.name", self.file_name)
        view = loader.load_module("module.name")
        return view.view_code(view, model)

class TemplateNode:
    def __init__(self, text = '', tab_size = 4):
        whitespace = re.match(r"\s*", text).group().expandtabs(tab_size)
        self.level = int(whitespace.count(' ') / tab_size)
        self.body = text.strip().split('#')[0]
        self.words = self.body.split()
        self.children = []
    
    def compile_node(self, _code = '', _code_indent = 0, _html_indent = 0):
        '''here be dragons'''
    
        tag = ''
    
        if self.body:
            try:
                compile(_code + '\n' +
                ' ' * _code_indent * 4 + '_result += str(' + self.body + ')\n' +
                ' ' * (_code_indent + 1 if self.body.endswith(':') else 0) * 4 + 'pass',
                '', 'exec' )
                _code += ' ' * _code_indent * 4 + '_result += "'+ ' ' * _html_indent * 4 + '" + str(' + self.body + ') + "\\n"\n'
            except:
                try:
                    compile(_code + '\n' +
                    ' ' * _code_indent * 4 + self.body + '\n' +
                    ' ' * (_code_indent + 1 if self.body.endswith(':') else 0) * 4 + 'pass', '', 'exec' )
                    _code += ' ' * _code_indent * 4 + self.body + '\n'
                    _code_indent += 1 if self.body.endswith(':') else 0
                except:
                    _code += ' ' * _code_indent * 4 + '_result += "' + ' ' * _html_indent * 4 + self.body + '\\n"\n'
                    tag_match = re.match('<([A-Za-z][A-Za-z0-9]*)>', self.body)
                    if tag_match:
                        tag = tag_match.group(1)
                    _html_indent += 1
        
        for child in self.children:
            _code = child.compile_node(_code, _code_indent, _html_indent)
        
        if tag:
            _code  += ' ' * _code_indent * 4 + '_result += "' + ' ' * (_html_indent - 1) * 4 + '</' + tag + '>\\n"\n'
            
        return _code

    def __call__(self, view, model):
        pass

    def __iadd__(self, node):
        if node.level == self.level + 1:
            self.children.append(node)
        elif node.level > self.level:
            self.children[-1] += node
            
        return self