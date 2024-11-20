import socket
import random
import hashlib

# Utility Functions
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    if gcd(e, phi) != 1:
        return None
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keypair():
    p = q = 1
    while not is_prime(p):
        p = random.randint(100, 1000)
    while not is_prime(q) or p == q:
        q = random.randint(100, 1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(encrypted_message, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])

def verify_signature(message, signature, public_key):
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    decrypted_signature = rsa_decrypt(signature, public_key)
    return decrypted_signature == hashed_message

# Server Code
def start_server():
    # Generate RSA key pair
    public_key, private_key = generate_keypair()
    print("Server RSA Key Pair Generated.")
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Set up socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 4455))
    server_socket.listen(1)
    print("Server is listening for connections...")

    conn, addr = server_socket.accept()
    print(f"\nConnection from {addr} established.")

    # Send server's public key to the client
    conn.sendall(str(public_key).encode())

    # Receive client's public key
    client_public_key = eval(conn.recv(4096).decode())
    print("Received Client Public Key:", client_public_key)

    # Receive encrypted message and signature
    encrypted_message = eval(conn.recv(4096).decode())
    signature = eval(conn.recv(4096).decode())

    # Decrypt the message
    received_message = rsa_decrypt(encrypted_message, private_key)

    # Verify the signature
    is_signature_valid = verify_signature(received_message, signature, client_public_key)

    # Respond to the client
    if is_signature_valid:
        print(f"\nClient Message: {received_message}. Signature is valid")
        response = f"Message received - {received_message}. Signature is valid."
    else:
        print(f"\nInvalid signature. Message integrity compromised.")
        response = "Invalid signature. Message integrity compromised."


    conn.sendall(response.encode())
    conn.close()

# Wrong key for to test for MitM attack
# client_public_key = (65537, 3233)  # Replace with actual client key during handshake

if __name__ == "__main__":
    start_server()
