def rail_fence_encrypt(plaintext, rails):
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    
    row = 0
    direction = 1  # 1 means down, -1 means up

    # Fill the fence matrix
    for i, char in enumerate(plaintext):
        fence[row][i] = char
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    encrypted_text = []
    for r in fence:
        encrypted_text.extend([char for char in r if char])

    return ''.join(encrypted_text)

def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    row = 0
    direction = 1
    for i in range(len(ciphertext)):
        fence[row][i] = '*'
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1

    decrypted_text = []
    row = 0
    direction = 1
    for i in range(len(ciphertext)):
        decrypted_text.append(fence[row][i])
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    return ''.join(decrypted_text)

plaintext = "HELLO"
rails = 3

ciphertext = rail_fence_encrypt(plaintext, rails)
print(f"Encrypted: {ciphertext}")

decrypted_text = rail_fence_decrypt(ciphertext, rails)
print(f"Decrypted: {decrypted_text}")
