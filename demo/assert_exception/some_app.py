import nutslib

def zeta(value):
    return 1/value

def delta():
    # Asserting zeta throws ZeroDivisionError..

    #;try:
    #;    zeta(0)
    #;except ZeroDivisionError:
    #;    pass

    x = zeta(10)
    return x + 1

delta()


