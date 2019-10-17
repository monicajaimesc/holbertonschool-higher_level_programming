#!/usr/bin/python3
"""
Module that contain a function that creates
an object from a Json File
"""
import json


def load_from_json_file(filename):
    with open(filename, mode='r') as f:
        return json.load(f)
