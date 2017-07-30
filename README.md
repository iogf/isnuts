# isnuts

A naive approach to test python code.

The isnuts lib permits you to inject python code as inline commentaries
for being executed later once the underlying application receives **--isnuts** argument.

It permit to test the application behavior in a flexible way and less prolix
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
[tau@sigma class_test]$ python some_class.py --isnuts
File:some_class.py
Line:12
Exception:<class 'AssertionError'> ()
3

~~~

The inline commentaries that start with #; before each statement get executed
when the application is run with **--isnuts** argument.

An example that tests if a method throws an exception would be:

~~~python
import nutslib

def beta(value):
    return 1/value

def alpha(value):
    # This case it will throw an assertion error.
    # Because beta function doesnt raise ZeroDivisionError at all.

    #;try:
    #;    beta(100)
    #;except ZeroDivisionError:
    #;    pass
    #;else:
    #;    raise Exception('Should throw ZeroDivisionError')
    

    return value 

alpha(10)

~~~

You would get:

~~~
[tau@sigma fail_exc_assertion]$ python some_app.py --isnuts
File:some_app.py
Line:18
Exception:<class 'Exception'> ('Should throw ZeroDivisionError',)

~~~

The following example shows how isnuts behaves with imports.

**some_app.py**

~~~python
import nutslib
import mymodule

def alpha(value):
    #;assert value == 1 or value == 2
    return value 

# This test comment is not going to be 
# called, it is in the main app.
#;print('it will not be printed.')
# Statements in the main module dont get traced unless
# they are executed in function/class contexts.
alpha(3)
~~~

Which imports...

**mymodule.py**

~~~python
# It will be executed when some_def gets defined.
#;print('In mymodule..')

def some_def():
    pass

~~~

Which would output:

~~~
[tau@sigma with_module]$ python some_app.py --isnuts
In mymodule..
File:/home/tau/projects/isnuts-code/demo/with_module/some_app.py
Line:6
Exception:<class 'AssertionError'> ()
~~~

Code commentaries get extracted from regions that are executed
in the application. Once extracted these are executed in the frame.f_globals
and frame.f_locals.

This approach of implementing tests would improve the ability
of others reading and understanding your code because the comment tests
would give a clue about what you're doing. It as well would improve your prediction
skills about how your code behaves with a given set of inputs.

Notice that if your underlying application receives arguments it shouldn't have issues with the 
**--isnuts** argument since isnuts automatically removes that argument from sys.argv
when your application is executed.

**Note:** It is in its early development stage, a lot can be done yet,
looking for suggestions :)


### Install

~~~
pip install isnuts
~~~

Then you're done.

**Note:** Would run on python3 only.




