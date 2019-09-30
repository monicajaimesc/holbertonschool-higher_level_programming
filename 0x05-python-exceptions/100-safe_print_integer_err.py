#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    # only accepts exceptions that you're meant to catch
    except Exception as error:
        sys.stderr.write("Exception: {:s}\n".format(str(error)))
        return (False)
    return (True)
