from itertools import takewhile
from os.path import abspath
import linecache
import sys
import re

def assert_exc(excpts, handle, *args, **kwargs):
    try:
        handle(*args, **kwargs)
    except excpts as e:
        pass
    else:
        raise AssertionError(
            'Should throw', excpts)

def assert_not_regex(regex, data):
    matches = re.search(regex, data)
    if matches:
        raise AssertionError(
           'Should not match: %s %s' % (regex, data))

def assert_regex(regex, data):
    matches = re.search(regex, data)
    if not matches:
        raise AssertionError(
            'Should match: %s %s' % (regex, data))

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
        tests = ''.join(reversed(list(tests)))
        frame.f_locals['assert_exc']   = assert_exc
        frame.f_locals['assert_regex'] = assert_regex
        frame.f_locals['assert_not_regex'] = assert_not_regex

        try:
            exec(tests, frame.f_globals, frame.f_locals)
        except Exception as err:
            self.display_exception(frame, err)

    def trace_calls(self, frame, event, arg):
        if event == 'line': 
            self.exec_code(frame)
        return self.trace_calls

    def get_comments(self, filename, start, end=0):
        inc = 1 if start < end else - 1
        for ind in range(start, end, inc):
            yield self.get_code(
                linecache.getline(filename, ind))

    def get_tests(self, filename, index):
        code = self.get_comments(filename, index - 1)
        return takewhile(lambda ind: ind, code)

    def get_code(self, data):
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

