#;print('It will be printed when the module is loaded.')

def beta(value):
    return 1/value

def alpha(value):
    # This case it will throw an assertion error.
    # Because beta function doesnt raise ZeroDivisionError if value==1.

    #;assert_exc((ZeroDivisionError, ), beta, 1)

    return value 

alpha(10)






