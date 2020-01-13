#!/usr/bin/python3
# takes in a letter and sends a POST request to an http

import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        parameter = sys.argv[1]
    else:
        parameter = ""

    values = {'q': parameter}
    # POST : to submit data to be processed to the server.
    status = requests.post(url, data=values)
    try:
        # status.json to process in python objects
        commit_data = status.json()
        if not commit_data:
            print('No result')
        else:
            print('[{}] {}'.format(commit_data.get('id'),
                                   commit_data.get('name')))
    except ValueError:
        print('Not a valid JSON')
