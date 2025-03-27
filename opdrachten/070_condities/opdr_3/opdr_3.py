# Opdracht 3 condities
# Naam student: Thijs Post
# Groep:

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de leeftijd van de bezoeker
leeftijd_bezoeker = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal de groep op basis van de leeftijd
for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_bezoeker <= max_leeftijd:
        # Toon de resultaten
        print(f"U behoort tot de groep {groep}")
        korting = kortings_percentages[groep]
        print(f"U krijgt {korting}% korting")
        prijs = normale_toegangsprijs * (1 - korting / 100)
        print(f"U betaalt daarom {prijs:.2f}")