#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return (False)
    '''
     True if value has been correctly printed
     (it means the value is an integer)
     '''
    return (True)
