# Opdracht 1 functies
# Naam student: Thijs Post
# Groep:


def volledige_naam(lijst_met_namen):
    # Loop door de lijst van dictionaries
    for naam in lijst_met_namen:
        # Voornaam, tussenvoegsel en achternaam ophalen
        voornaam = naam["voornaam"]
        tussenvoegsel = naam["tussenvoegsel"]
        achternaam = naam["achternaam"]
        
        # Als er een tussenvoegsel is, voeg dit toe aan de volledige naam
        if tussenvoegsel:
            print(f"{voornaam} {tussenvoegsel} {achternaam}")
        else:
            print(f"{voornaam} {achternaam}")

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
