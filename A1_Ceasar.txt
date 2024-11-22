# Implement Caesar cipher

def caesar_cipher(plain_text, shift):
    result = []

    for char in plain_text:
        if char.isupper():
            result.append(chr((ord(char) + shift - 65)%26 + 65))
        elif char.islower():
            result.append(chr((ord(char) + shift - 97)%26 + 97))
        else: 
            result.append(char)
        
    return ''.join(result)

plain_text = "i am AI"

encrypted_text = caesar_cipher(plain_text, 3)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, -3)
print(f"Decrypted Text: {decrypted_text}")


'''
TC = O(n); n = len(plain_text)
Adv:
    - Simple
    - Quick
Disadv: 
    - only 26 tries reqd to crack cipher
    - predictable pattern
    - ltd applicn
'''