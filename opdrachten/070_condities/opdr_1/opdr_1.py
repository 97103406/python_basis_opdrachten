# Opdracht 1 condities
# Naam student: Thijs Post
# Groep:

# Vraag de gebruiker om de lengte van de rechthoekzijden van de driehoek
zijde1 = float(input("Geef de lengte van de eerste rechthoekzijde: "))
zijde2 = float(input("Geef de lengte van de tweede rechthoekzijde: "))

# Bereken de lengte van de schuine zijde (Pythagoras)
schuine_zijde = (zijde1**2 + zijde2**2) ** 0.5

# Print het resultaat
print(f"De schuine zijde van de driehoek is: {schuine_zijde:.2f}")