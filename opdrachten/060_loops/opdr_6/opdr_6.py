# Opdracht 3 input functie
# Naam student: thijs post
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Beginlijst van pizza's
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()

# Voeg een pizza toe
pizzas.append('yo-favorito')

# Verwijder de pizza die je het minst lekker vindt
pizzas.remove('olivio')

# Print de eerste 3 pizza's
print(pizzas[:3])

# Print de middelste pizza
print([pizzas[len(pizzas) // 2]])

# Print de laatste 3 pizza's
print(pizzas[-3:])
