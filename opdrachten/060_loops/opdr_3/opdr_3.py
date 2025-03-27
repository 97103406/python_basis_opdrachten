# Opdracht 3 input functie
# Naam student: thijs post
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Maak een lege lijst voor de resultaten
resultaten = []

# Gebruik een for-loop en range om de getallen van 3 tot 81 (inclusief) te genereren
for i in range(3, 82, 3):
    resultaat = (i ** 2) / 3  # Kwadraat van i en gedeeld door 3
    resultaten.append(resultaat)

# Print de lijst met resultaten
print(resultaten)
