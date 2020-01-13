#!/usr/bin/python3
# Write a Python script that fetches https://intranet.hbtn.io/status

import urllib.request
# import textwrap

with urllib.request.urlopen('https://intranet.hbtn.io/status') as status:
    print('Body response:')
    # read everything that the request return
    text = status.read()
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
    # we can have it decoded so we can print it out to the user
    print('\t- utf8 content: {}'.format(text.decode('utf-8')))
    decode_text = text.decode('utf-8')
    # to see the json file use textwrap module
    # print(textwrap.fill(decode_text, width=50))
