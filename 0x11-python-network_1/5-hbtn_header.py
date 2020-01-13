#!/usr/bin/python3
# takes in a URL, send a request to the URL and display X-Request-Id

import requests
import sys

if __name__ == '__main__':

    parameter = sys.argv[1]
    status = requests.get(parameter)
    print(status.headers['X-Request-Id'])
