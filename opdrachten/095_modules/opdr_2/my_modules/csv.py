#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv

# csv.py
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print(f"Het bestand {file_path} werd niet gevonden.")
        return None

def filter(persoon, filterveld, filter):
    filtered_list = []
    for p in persoon:
        if p[filterveld].lower().startswith(filter.lower()):
            filtered_list.append(p)
    return filtered_list
