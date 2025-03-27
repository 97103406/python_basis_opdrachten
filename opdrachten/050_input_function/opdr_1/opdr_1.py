# Opdracht 1 input function
# Naam student: thijs post
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


import math

# Vraag de lengtes van de twee rechthoekzijden op
zijde1 = float(input("Geef de lengte van de eerste zijde\n"))
zijde2 = float(input("Geef de lengte van de tweede zijde\n"))

# Bereken de lengte van de schuine zijde met behulp van de stelling van Pythagoras
schuine_zijde = math.sqrt(zijde1**2 + zijde2**2)

# Print het resultaat
print(f"\nDe lengte van de schuine zijde is: {schuine_zijde}")
