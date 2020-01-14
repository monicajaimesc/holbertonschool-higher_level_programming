#!/usr/bin/python3
# sends a search request to the Star Wars API

import requests
import sys

if __name__ == '__main__':
    parameter = sys.argv[1]
    response = requests.get('https://swapi.co/api/people/?search={}'
                            .format(parameter))
    list_ = response.json()
    print('Number of results: {}'.format(list_.get('count')))
    for i in list_.get('results'):
        print(i.get('name'))
