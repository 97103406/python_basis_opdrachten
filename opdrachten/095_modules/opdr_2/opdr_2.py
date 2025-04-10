# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

# opdr_1.py
from my_modules.csv import filter

# Voorbeeldlijst van personen
personen = [
    {"voornaam": "Jan", "achternaam": "Van Der Vliet", "plaats": "Amsterdam"},
    {"voornaam": "Piet", "achternaam": "De Vries", "plaats": "Rotterdam"},
    {"voornaam": "Griet", "achternaam": "Van Der Pol", "plaats": "Den Haag"},
    {"voornaam": "Jan Jaap", "achternaam": "Siewers", "plaats": "Utrecht"}
]

def main():
    # Filter op voornaam die begint met 'Ja'
    print("Filter op voornaam die begint met 'Ja':")
    filtered_personen = filter(personen, "voornaam", "Ja")
    for p in filtered_personen:
        print(f"{p['voornaam']} {p['achternaam']}")
    
    print("\nFilter op voornaam die begint met 'Pie':")
    # Filter op voornaam die begint met 'Pie'
    filtered_personen = filter(personen, "voornaam", "Pie")
    for p in filtered_personen:
        print(f"{p['voornaam']} {p['achternaam']}")

    print("\nFilter op plaats die begint met 'd':")
    # Filter op plaats die begint met 'd'
    filtered_personen = filter(personen, "plaats", "d")
    for p in filtered_personen:
        print(f"{p['voornaam']} {p['achternaam']}")

if __name__ == '__main__':
    main()
