import nutslib

def beta(value):
    return 2

def alpha(value):
    # This case it will throw an assertion error.
    #;assert beta('ooo') == 1
    n = beta(10) + 1
    
    # Justing checking n..
    #;print('The value for n:', n)
    return n

alpha(10)



