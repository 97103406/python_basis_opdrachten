
# Opdracht 3 Tekst opslaan
# Naam student: thijs
# Groep: ho

# Functie om de tekst te encrypten
def encrypt(text):
    encrypted_text = ""
    for char in text:
        # Controleer of het een letter is
        if char.isalpha():
            # Verschuiif de letter 5 plaatsen
            shift = 5
            # Bepaal de ASCII-code van de letter en pas de verschuiving toe
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Voeg niet-lettertekens zonder verandering toe
            encrypted_text += char
    return encrypted_text

# Functie om de tekst te decrypten
def decrypt(text):
    decrypted_text = ""
    for char in text:
        # Controleer of het een letter is
        if char.isalpha():
            # Verschuiif de letter 5 plaatsen in de andere richting
            shift = 5
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            # Voeg niet-lettertekens zonder verandering toe
            decrypted_text += char
    return decrypted_text

# Vraag de gebruiker om de tekst in te voeren
input_text = input("Geef de tekst die je wilt encrypten: ")

# Encrypt de tekst
encrypted = encrypt(input_text)
print("Encrypted tekst: ", encrypted)

# Decrypt de tekst
decrypted = decrypt(encrypted)
print("Decrypted tekst: ", decrypted)


