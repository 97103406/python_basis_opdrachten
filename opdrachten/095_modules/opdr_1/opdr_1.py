# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...


# csv.py
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print(f"Het bestand {file_path} werd niet gevonden.")
        return None
