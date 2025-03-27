# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    # Open het bestand in 'append' modus, zodat de tekst wordt toegevoegd als het bestand bestaat
    with open(afile, 'a') as file:
        file.write(atext + '\n')  # Voeg een nieuwe regel toe na de tekst

# Voorbeeld van het gebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
