#!/usr/bin/python3
# takes a URL and an email, sends a POST request to the URL with the email as a parameter

import sys
import urllib.request
import urllib.parse

if "__main__" == __name__:

    parameter1 = sys.argv[1]
    parameter2 = sys.argv[2]
    values = {'email': parameter2}
    email = urllib.parse.urlencode(values).encode('ascii')
    # sends a POST request to the URL as parameter
    with urllib.request.urlopen(parameter1, email) as status:
        text = status.read()
        decode_text = text.decode('utf-8')
        print(decode_text)

