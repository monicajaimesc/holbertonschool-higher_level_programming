#!/usr/bin/python3
# ses the Github API to display your id

import requests
import sys

if __name__ == '__main__':
    parameter1 = sys.argv[1]
    parameter2 = sys.argv[2]
    response = requests.get('https://api.github.com/user'
                            .format(parameter1, parameter2))
    decode = response.json()
    print(decode.get('id'))
