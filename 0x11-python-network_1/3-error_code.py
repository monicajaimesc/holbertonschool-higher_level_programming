#!/usr/bin/python3
# takes in  a URL, sends a request and display the response body

import sys
import urllib.request
from urllib.error import HTTPError

if "__main__" == __name__:
    parameter1 = sys.argv[1]

    try:
        with urllib.request.urlopen(parameter1) as status:
            pass
    # HTTP response from the server
    except HTTPError as error:
        print('Error code: {}'.format(error.code))
