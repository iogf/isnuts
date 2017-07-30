import linecache
import sys

class Parser:
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
        elif not data.strip().rstrip():
            return '\n'
        return None

class Tester:
    def __init__(self):
        self.parser = Parser()
        sys.settrace(self.trace_calls)

    def trace_lines(self, frame, event, arg):
        if event != 'line': 
            return

        filename = frame.f_globals.get('__file__', 
        frame.f_globals.get('__name__'))

        if not filename: return

        tests = self.parser.get_tests(
                filename, frame.f_lineno)

        if not tests: return
        print('File:', frame.f_globals['__file__'])
        print('Line:', frame.f_lineno)
        exec(tests, frame.f_globals, frame.f_locals)
        print()

    def trace_calls(self, frame, event, arg):
        return self.trace_lines

if __name__ != '__main__':
    try:
        sys.argv.remove('--isnuts')
    except ValueError:
        pass
    else:
        tester = Tester()

