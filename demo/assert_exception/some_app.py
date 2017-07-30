
def zeta(value):
    return 1/value

def delta():
    # Asserting zeta throws ZeroDivisionError..

    #;try:
    #;    zeta(0)
    #;except ZeroDivisionError:
    #;    pass

    # It will print an exception and not pass in the test.
    #;assert zeta(10) < 0
    x = zeta(10)
    return x + 1

delta()




