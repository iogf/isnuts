from os.path import abspath
import linecache
import sys

def assert_exc(excpts, handle, *args, **kwargs):
    try:
        handle(*args, **kwargs)
    except excpts as e:
        pass
    else:
        raise AssertionError(
            'Should throw', excpts)

class Tester:
    """
    Used to keep track of function calls and execute
    code comments.
    """

    def __init__(self):
        sys.settrace(self.trace_calls)

    def display_exception(self, frame, err):
        print('File:', abspath(frame.f_globals.get('__file__')))
        print('Line:', frame.f_lineno)
        print('Exception:', err.__class__, err.args)

    def exec_code(self, frame):
        tests = self.get_tests(abspath(
        frame.f_globals.get('__file__')), frame.f_lineno)

        frame.f_locals['assert_exc'] = assert_exc

        try:
            exec(tests, frame.f_globals, frame.f_locals)
        except Exception as err:
            self.display_exception(frame, err)

    def trace_calls(self, frame, event, arg):
        if event == 'line': 
            self.exec_code(frame)
        return self.trace_calls

    def get_tests(self, filename, line):
        code = ''

        while True:
            line = line - 1
            data = self.get_code(filename, line)
            if not data: 
                return code
            code = '%s%s' % (data, code)

    def get_code(self, filename, line):
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


