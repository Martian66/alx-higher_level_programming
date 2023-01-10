#!/usr/bin/python3
"""A script that adds all arguments to a python list and save them to a file"""

import json
# a python module
import os.path
# module used to process and merge the files paths
import sys
# used to access system-specific parameters and functions
from sys import argv
""" Importing a list in python that contains all the command-line
arguments passed to the script"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# importing and saving text file to json file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
# importing and loading text file to json file

filename = "add_items.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

    for index in argv[1:]:
        json_list.append(index)

        save_to_json_file(json_list, filename)
