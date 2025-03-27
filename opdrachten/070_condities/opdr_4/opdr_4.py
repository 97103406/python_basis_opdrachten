# Lijst met toppings
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van de beschikbare toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze te maken
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Controleer of de keuze geldig is en geef de bijbehorende prijs weer
gevonden = False
for topping, prijs in toppings:
    if keuze.lower() == topping:
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        gevonden = True
        break

# Als de keuze niet geldig is
if not gevonden:
    print("Uw keuze zit niet in ons assortiment.")
