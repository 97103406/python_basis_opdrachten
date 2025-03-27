# Opdracht 4 Tekst opslaan
# Naam student: Thijs Post
# Groep:


# Vragenlijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Lijst om de gegevens van feestgangers op te slaan
feestgangers = []

# Functie om de gegevens van een feestganger op te slaan
def stel_vragen():
    gegevens = {}
    for i, vraag in enumerate(vragen):
        antwoord = input(f"{i+1}. {vraag}\n")
        if i == 0:
            gegevens['voornaam'] = antwoord
        elif i == 1:
            gegevens['achternaam'] = antwoord
        elif i == 2:
            gegevens['drank'] = antwoord
        elif i == 3:
            gegevens['eten'] = antwoord
    feestgangers.append(gegevens)

# Vraag of er meerdere feestgangers zijn
while True:
    stel_vragen()
    
    # Vraag of de gebruiker nog iemand wil toevoegen
    doorgaan = input("Wil je nog iemand toevoegen? (ja/nee): ").strip().lower()
    if doorgaan != 'ja':
        break

# Bedankje
print("\nBedankt voor het invullen!")
print("See you at the party.\n")

# Sla de gegevens op in een tekstbestand
with open('feestgangers.txt', 'w') as f:
    for feestganger in feestgangers:
        f.write("----\n")
        for sleutel, waarde in feestganger.items():
            f.write(f"{sleutel}: {waarde}\n")
