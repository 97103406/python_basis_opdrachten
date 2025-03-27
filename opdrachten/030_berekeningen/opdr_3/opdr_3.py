# Opdracht 3 tekstfuncties
# Naam student: thijs post
# Groep:

# opdr_3.py

# Variabelen
x = 1  # Pas deze waarde aan voor verschillende tests

# Formule: y = 4x^3 - 2x^2 - 1
y = (4 * (x ** 3)) - (2 * (x ** 2)) - 1

# Print resultaat
print(f"De uitkomst is: {y}")

# Test met andere waarden
for x in [2, 0]:  
    y = (4 * (x ** 3)) - (2 * (x ** 2)) - 1
    print(f"De uitkomst is: {y}")
