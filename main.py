#!/usr/bin/env python
# coding: utf-8

import os
import json


def clear_name(name, replace_settings):
    """Cleans up a given dirty_name by replacing certain positions
     or substrings in the name based on the provided replace_settings"""

    for position in replace_settings:
        name = name.replace(position, replace_settings[position])

    # Return the cleaned name, stripping any leading or trailing whitespace
    return name.strip()


def main():
    """Cleans all filenames in the current directory."""
    # User has one last chance to abort changing filenames
    user_action = input("You are about to clean all the filenames in the directory:\n"
                        + os.getcwd()
                        + '\nDo you want to proceed? (y/n)\n')

    if user_action.lower() == 'y':
        # Loading the JSON file
        file_location = os.path.dirname(os.path.abspath(__file__))
        settings_file = os.path.join(file_location, 'symbols_to_replace.json')
        with open(settings_file) as file:
            settings = json.load(file)

        # Iterate over each filename in the current directory
        for filename in os.listdir():
            clean_name = clear_name(filename, settings)
            os.rename(os.path.join(os.getcwd(), filename),
                      os.path.join(os.getcwd(), clean_name))
            print(f"Old name: {filename}\n"
                  f"New name: {clean_name}"
                  f"\n-----")
    else:
        pass


if __name__ == "__main__":
    main()
