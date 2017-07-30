# Isnuts

A naive approach to test python code.

The isnuts lib permits you to inject python code as inline commentaries these
will be executed before each one of the statements it preceds.

It permit to test the application behavior in a flexible way
than writing tests in the standard approach.

In the actual approach for TDD tests one would follow the approach of writing tests
for each one of its functions then writing the functions to pass the tests. 

It would be done in separate files, with isnuts approach it permits you to write your tests
inside your functions as comments then go adding code to the functions to pass the tests.

You would just need a file named tests.py that launches your
application using isnuts lib.

One of the advantages of isnuts is: if you have to refactor functions or rename them you can just 
quickly change the function tests while you change the function! It would speed up development
yet making your code more readable since the comments(which are merely python code) would help others
to understand what you're doing.

Other advantage of this approach consists of the fact of you having access to the function's scope
it permits you to better test how functions behave since you can test function B from function A
it would give you more power in predicting the behavior of the code.

### The isnuts approach to TDD

The sequence below examplifies the approach:

You first need a tests.py file that will launch your application, but this one imports nutslib
to execute your tests.

**tests.py**

~~~python
from nutslib import Tester
tester = Tester()

# Just imports your application to be tested, here you can
# decide to test your application entirely or just parts of it.
# You could have more than one tests.py file which tests separately
# parts of your code.
import app
~~~

**app.py**

~~~python
def some_function(value0, value1, ...)
    # These #; code comments will be executed when you run your tests.py file..
    #;assert some_function(1, 2, 3, ..) == some_returned_value0
    #;assert some_function(1, 4, 3, ..) == some_returned_value1
    #;assert some_function(1, 2, 3, ..) == some_returned_value2

~~~

Now you have implemented your tests for your function, you can just
start writing your code for the function and go checking if it passes your tests :)

**app.py**

~~~python
def some_function(value0, value1, ...)
    # These #; code comments will be executed when you run your tests.py file..
    #;assert some_function(1, 2, 3, ..) == some_returned_value0
    #;assert some_function(1, 4, 3, ..) == some_returned_value1
    #;assert some_function(1, 2, 3, ..) == some_returned_value2
    
    # code...
    return return_value
~~~

After that, you just run your **tests.py** file.

~~~
python tests.py
~~~

Then you would get information where your tests fail.

### Basic example

First of all you implement a tests file which launches your application and imports
the Tester class.

**tests.py**

~~~
from nutslib import Tester
tester = Tester()

# Initialize the application.
import some_app

~~~


Where you have:

**some_app.py**

~~~python
import nutslib

def beta(value):
    return 1

def alpha(value):
    # Testing beta from alpha..
    #;print('The alpha function got:', value)
    #;assert beta(1) == 1
    #;assert beta(2) == 1
    #;assert beta('ooo') == 1
    n = beta(10) + 1
    
    # Justing checking n..
    #;print('The value for n:', n)
    return n

alpha(10)


~~~

You want to test some_app.py then you run:

~~~
python tests.py
~~~

You'll get all statements that start with '#;' executed in the scope.

~~~
[tau@sigma basic_assert]$ python tests.py 
The alpha function got: 10
The value for n: 2

~~~

### Exceptions

The following example shows how to make sure a function
raises an exception.

**tests.py**

~~~python
from nutslib import Tester
tester = Tester()

# Initialize the application.
import some_app
~~~

**some_app.py**

~~~python
#;print('It will be printed when the module is loaded.')

def beta(value):
    return 1/value

def alpha(value):
    # This case it will throw an assertion error.
    # Because beta function doesnt raise ZeroDivisionError if value==1.

    #;assert_exc((ZeroDivisionError, ), beta, 0)

    return value 

alpha(10)

~~~

You would get:


~~~
[tau@sigma fail_exc_assertion]$ python tests.py 
It will be printed when the module is loaded.
File: /home/tau/projects/isnuts-code/demo/fail_exc_assertion/some_app.py
Line: 12
Exception: <class 'AssertionError'> ('Should throw', (<class 'ZeroDivisionError'>,))

~~~


This example shows how it would be with a class:

### With classes

**tests.py**

~~~python
from nutslib import Tester
tester = Tester()

# Initialize the application.
import some_class
some_class.main()
~~~

**some_class.py**

~~~python
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

You would get:

~~~
[tau@sigma class_test]$ python tests.py 
File:/home/tau/projects/isnuts-code/demo/class_test/some_class.py
Line:12
Exception:<class 'AssertionError'> ()
3

~~~



