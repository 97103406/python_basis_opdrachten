# Opdracht 2 berekeningen
# Naam student: thijs post
# Groep:

# Hier komt je code...

# Maak een lijst met de gasten
gasten = ["thijs", "Paul", "Kees", "Marie", "Hilda"]

# Print de lijst met gasten
print("Lijst van gasten:", gasten)

# Marie belt af, dus we halen haar uit de lijst
gasten.remove("Marie")

# Print de lijst zonder Marie
print("Lijst van gasten na Marie's afmelding:", gasten)

# George belt, en hij wil naast Kees zitten
# Voeg George toe na Kees
kees_index = gasten.index("Kees")  # Vind de index van Kees
gasten.insert(kees_index + 1, "George")  # Voeg George toe direct na Kees

# Print de nieuwe lijst met George erbij
print("Lijst van gasten na George's toevoeging:", gasten)
