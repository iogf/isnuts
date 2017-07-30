#;print('It will be printed when the module is loaded.')

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





