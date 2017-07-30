# It will be executed when the module is loaded.
#;print('In mymodule..')

def gamma(value):
    return value + 1

# Testing gamma here..
#;print('It will be printed when beta is called.')
#;assert gamma(10) == 12

# When the function beta gets called, isnuts lib
# collects all test commentaries upwards.

def beta():
    # Will not pass in the tests.
    #;assert gamma(10) == 12
    pass

