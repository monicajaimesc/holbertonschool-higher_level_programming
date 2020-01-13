#!/usr/bin/python3
#  takes in a URL, sends a request to the URL and displays the variable value

import sys
import urllib.request

if "__main__" == __name__:

    parameter = sys.argv[1]
    with urllib.request.urlopen(parameter) as status:
        # unique request ID, represented by a UUID is
        # generated at each HTTP request
        print(status.headers['X-Request-Id'])
