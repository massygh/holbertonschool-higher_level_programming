#!/usr/bin/python3
"""Module to save a json file"""
import sys
from "5-save_to_json_file" import save_to_json_file
from "6-load_from_json_file" import load_from_json_file

def add_to_list_and_save(args):
    try:
        # Load existing list from file or create an empty list
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    # Add arguments to the list
    existing_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(existing_list, "add_item.json")

if __name__ == "__main__":
    # Remove the script name from arguments
    args = sys.argv[1:]
    add_to_list_and_save(args)
