#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status

import requests

if "__main__" == __name__:
    status = requests.get('https://intranet.hbtn.io/status')
    # u'{"type":"User"...'
    status_text = status.text
    print('Body response:')
    print('\t- type: {}'.format(type(status_text)))
    print('\t- content: {}'.format(status_text))
