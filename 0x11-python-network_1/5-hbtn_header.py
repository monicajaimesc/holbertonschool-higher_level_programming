#!/usr/bin/python3
# takes in a URL, send a request to the URL and display X-Request-Id

import requests
import sys

if __name__ == '__main__':

    parameter = sys.argv[1]
    status = requests.get(parameter)
    # get access to a dictionary (headers is the dictionary)
    print(status.headers.get('X-Request-Id'))
