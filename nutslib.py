"""

"""

import linecache
import sys
import os

class Parser:
    """
    Used to extract code comments.
    """

    def get_tests(self, filename, line):
        code = ''
        while True:
            line = line - 1
            data = self.is_test(filename, line)
            if not data:
                return code
            code = '%s%s' % (data, code)

    def is_test(self, filename, line):
        data = linecache.getline(filename,  line)
        chks = data.split('#;')
        if len(chks) == 2:
            return chks[1]
        elif not data:
            return None
        elif not data.strip().rstrip():
            return '\n'
        elif data.strip().startswith('#'):
            return data
        return None

class Tester:
    """
    Used to keep track of function calls and execute
    code comments.
    """

    def __init__(self):
        self.parser = Parser()
        sys.settrace(self.trace_calls)

    def exec_code(self, frame):
        filename = os.path.abspath(frame.f_globals.get('__file__'))
        tests = self.parser.get_tests(filename, frame.f_lineno)

        try:
            exec(tests, frame.f_globals, frame.f_locals)
        except Exception as err:
            print('File:%s\nLine:%s\nException:%s %s' % (
                filename, frame.f_lineno, 
                    err.__class__, err.args))

    def trace_calls(self, frame, event, arg):
        if event == 'line': 
            self.exec_code(frame)
        return self.trace_calls

if __name__ != '__main__':
    try:
        sys.argv.remove('--isnuts')
    except ValueError:
        pass
    else:
        tester = Tester()

