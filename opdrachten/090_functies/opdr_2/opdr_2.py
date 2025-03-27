

# Opdracht 1 functies
# Naam student: Thijs post
# Groep:


def kilometers_naar_miles(km):
    # Kilometers omrekenen naar miles
    return km / 1.609344

def miles_naar_kilometers(miles):
    # Miles omrekenen naar kilometers
    return miles * 1.609344

kilometers = 1223
miles = 867

print(f"{kilometers} kilometers = {kilometers_naar_miles(kilometers)} miles")
print(f"{miles} miles = {miles_naar_kilometers(miles)} kilometers")
