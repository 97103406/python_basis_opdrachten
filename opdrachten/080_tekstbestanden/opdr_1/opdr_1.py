# Opdracht 2 tekstbestanden
# Naam student: Thijs Post
# Groep:

# Functie om de enquêtevragen te stellen en antwoorden op te slaan
def start_enquete():
    # Openen van het bestand in schrijfmodus
    with open("enquete_resultaten.txt", "w") as file:
        # Vraag 1
        vraag1 = input("Wat vind je van de huidige regering? ")
        file.write(f"1. Wat vind je van de huidige regering? {vraag1}\n")
        
        # Vraag 2
        vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
        file.write(f"2. Wat vind je van de Python-lessen tot nu toe? {vraag2}\n")
        
        # Vraag 3
        vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")
        file.write(f"3. Wat vind jij de mooiste stad van Nederland? {vraag3}\n")
    
    print("De antwoorden zijn opgeslagen in 'enquete_resultaten.txt'.")

# Hoofdfunctie die de enquête start
def main():
    start_enquete()

# Programma uitvoeren
if __name__ == "__main__":
    main()
