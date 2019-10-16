#!/usr/bin/python3
"""
Module with a script that adds arguments
to a Python list saved in a file
"""

import sys
import os


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
if os.path.exists(filename):
    # if it exists, called it, otherwise
    # make a new one
    the_list = load_from_json_file(filename)
else:
    with open(filename, mode='w') as f:
        the_list = []
        save_to_json_file([], filename)

for arg in range(1, len(sys.argv)):
    the_list.append(sys.argv[arg])
    save_to_json_file(the_list, filename)
