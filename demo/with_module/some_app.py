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




