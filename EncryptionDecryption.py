message = input("Enter a word: ")
shift = 3

secret = ""
for letter in message:
    if letter.isalpha():
        start = 65 if letter.isupper() else 97
        secret += chr((ord(letter) - start + shift) % 26 + start)
    else:
        secret += letter

original = ""
for letter in secret:
    if letter.isalpha():
        start = 65 if letter.isupper() else 97
        original += chr((ord(letter) - start - shift) % 26 + start)
    else:
        original += letter

print("Encrypted:", secret)
print("Decrypted:", original)