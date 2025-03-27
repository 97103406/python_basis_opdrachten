# Opdracht 1 functies
# Naam student: thijs post
# Groep:


import math

def kubus_vol(m):
    # Volume van een kubus is m^3 (zijde^3)
    return m ** 3

def bol_vol(r):
    # Volume van een bol is (4/3) * pi * r^3
    return (4/3) * math.pi * r ** 3

zijde = 5
radius = 4

print("De inhoud van de kubus is:", kubus_vol(5))
print("De inhoud van de bol is:", bol_vol(4))
