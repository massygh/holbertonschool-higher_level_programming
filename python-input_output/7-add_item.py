#!/usr/bin/python3
"""Module to save a json file"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_to_list_and_save(args):
    existing_list = load_from_json_file("add_item.json")
    existing_list.extend(args)
    save_to_json_file(existing_list, "add_item.json")

if __name__ == "__main__":
    args = sys.argv[1:]
    add_to_list_and_save(args)
