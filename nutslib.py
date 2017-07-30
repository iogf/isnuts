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
        return None

class Tester:
    def __init__(self):
        self.parser = Parser()
        sys.settrace(self.trace_calls)

    def exec_code(self, frame, globals, locals):
        pass

    def trace_lines(self, frame, event, arg):
        if event != 'line': 
            return

        filename = frame.f_globals.get('__file__', 
        frame.f_globals.get('__name__'))
        data = linecache.getline(filename,  frame.f_lineno)

        if not filename: return

        tests = self.parser.get_tests(
                filename, frame.f_lineno)

        if not tests: return
        print('File:', frame.f_globals['__file__'])
        print('Line:', frame.f_lineno)
        exec(tests, frame.f_globals, frame.f_locals)
        print('\n\n')

    def trace_calls(self, frame, event, arg):
        return self.trace_lines
        # module name
        # print(frame.f_globals['__name__'])
        # print(event)


        # dict locals.
        # if frame.f_locals:
            # print(type(frame.f_locals))

if '--isnuts' in sys.argv:
    tester = Tester()

    

