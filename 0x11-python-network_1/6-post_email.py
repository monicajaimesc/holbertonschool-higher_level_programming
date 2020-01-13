#!/usr/bin/python3
# takes in a URL and an email address, send a POST request to the URL

import requests
import sys

if __name__ == '__main__':

    parameter1 = sys.argv[1]
    parameter2 = {'email': sys.argv[2]}
    status = requests.post(parameter1, data=parameter2)
    print(status.text)
