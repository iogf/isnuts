# isnuts

A naive approach to test python code.

The isnuts lib permits you to inject python code as inline commentaries
for being executed later once the underlying application receives **--isnuts** argument.

It permits to test the application behavior in a flexible way and less prolix
than writing tests in the standard approach.

### Basic code

The following code uses python unittest module to test MyClass methods.

~~~python
import unittest
from myclass import MyClass

class TestMyClassMethods(unittest.TestCase):
    def test_method0(self):
        self.assertEqual(MyClass().method0('oo'), 1)

    def test_method1(self):
        self.assertEqual(MyClass().method0('oo'), 3)

if __name__ == '__main__':
    unittest.main()
~~~

Where the code for the application could be something like:

~~~python
import nutslib

class MyClass:
    def method0(self, value):
        return 1
    def method1(self, value):
        return 2

def main():
    x = MyClass()
    print(x.method1('oo') + x.method0('oo'))

if __name__ == '__main__':
    main()
~~~

With isnuts approach, the tests would be included in the myclass module
and these would be merely commentaries.

~~~python
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

~~~

Once running the above example with:

~~~
python myclass.py --isnuts

~~~

You would get:

~~~
[tau@sigma class_test]$ python some_class.py --isnuts
File:some_class.py
Line:12
Exception:<class 'AssertionError'> ()
3

~~~



