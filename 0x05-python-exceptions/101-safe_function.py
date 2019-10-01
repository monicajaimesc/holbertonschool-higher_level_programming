#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # fct: pointer to a function
        result = fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {:s}\n".format(str(error)))
        return (None)
    return (result)
