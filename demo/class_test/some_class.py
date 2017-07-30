import nutslib

class MyClass:
    def method0(self, value):
        # Notice you can test method1 from here too.
        # It wouldnt pass in the tests because
        # self.method1 returns always 2.
        #;assert self.method1(10) == 3
        
        # Just printing the value..
        #;print('The value:', value)
        return 1

    def method1(self, value):
        return 2

def main():
    x = MyClass()

    # Testing method0 and method1 using x instance.
    #;assert x.method0('uuuu') == 1
    #;assert x.method1('oooooo') == 2
    #;assert (x.method0('oo') + x.method1('oo')) == 3
    print(x.method1(10) + x.method0(100))

if __name__ == '__main__':
    main()
