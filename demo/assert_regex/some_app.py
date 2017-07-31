def alpha(value):
    #; assert_regex('[a-z]+', alpha('abc'))
    # It passes...
    #; assert_not_regex('uue', alpha(''))

    # This one would fail...
    #; assert_regex('^[a-z]+$', alpha('UU'))

    return 'uu' + value

alpha('oo')







