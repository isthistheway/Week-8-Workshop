def f_to_c(f):
    '''Convert argument temperature from fahrenheit to celsius.'''
    if (isinstance(f, int) or isinstance(f, float)):
        return (f-32)*(5/9)
    else:
        raise TypeError("Only int or float is allowed.")
    
def c_to_f(c):
    '''Convert argument temperature from celsius to fahrenheit.'''
    if (isinstance(c, int) or isinstance(c, float)):
        return c*(9/5) + 32
    else:
        raise TypeError("Only int or float is allowed.")