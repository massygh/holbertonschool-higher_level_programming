#!/usr/bin/python3
# module: 7-add_item.py
"""Add all arguments to a Python list, and then save them to a file."""
import sys

# Importer les fonctions spécifiques depuis les fichiers Python
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_to_list_and_save(args):
    existing_list = load_from_json_file("add_item.json")
    existing_list.extend(args)
    save_to_json_file(existing_list, "add_item.json")
