# Opdracht 1 lists
# Naam student: thijs post
# Groep:

# Maak een lege lijst
mylist = []

# Maak 4 dictionaries met gegevens van personen
dict_1 = {"id": 0, "voornaam": "Jan", "achternaam": "Jansen"}
dict_2 = {"id": 1, "voornaam": "Emma", "achternaam": "Peters"}
dict_3 = {"id": 2, "voornaam": "Lars", "achternaam": "Smit"}
dict_4 = {"id": 3, "voornaam": "Sophie", "achternaam": "Vermeulen"}

# Voeg de dictionaries toe aan de lijst met een list-methode
mylist.extend([dict_1, dict_2, dict_3, dict_4])

# Print de volledige naam van de 2e persoon
print(mylist[1]["voornaam"], mylist[1]["achternaam"])
