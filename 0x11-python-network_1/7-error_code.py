#!/usr/bin/python3
# takes in a URL, sends a request to the URL and displays the body response

import requests
import sys

if __name__ == '__main__':
    parameter = sys.argv[1]
    # requests provide access to the full range of HTTP verbs:
    # Get for this case
    response = requests.get(parameter)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
