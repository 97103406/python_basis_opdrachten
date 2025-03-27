# Opdracht 3 input functie
# Naam student: thijs post
# Groep:

# Hier komt je code...

# Vraag de gebruiker om vijf steden in te vullen
steden = []
for i in range(5):
    stad = input(f"Voer stad {i+1} in: ")
    steden.append(stad)

# Sorteer de lijst in omgekeerde volgorde
steden.sort(reverse=True)

# Print de gesorteerde lijst
print("Gesorteerde lijst van steden:", steden)
