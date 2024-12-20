import socket
import random
import hashlib

# Utility Functions
def generate_keypair():
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
        for d in range(1, phi):
            if (e * d) % phi == 1:
                return d
        return None

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

def generate_signature(message, private_key):
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    return rsa_encrypt(hashed_message, private_key)

# Client Code
def start_client():
    # Generate RSA key pair
    public_key, private_key = generate_keypair()
    print("Client RSA Key Pair Generated.")
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Set up socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 4455))
    print(f"\nConnection successfully established with Server")

    # Receive server's public key
    server_public_key = eval(client_socket.recv(4096).decode())
    print("Received Server Public Key:", server_public_key)

    # Send client's public key to the server
    client_socket.sendall(str(public_key).encode())

    # Input message
    message = input("\nEnter the message to be sent: ")

    # Encrypt the message with server's public key
    encrypted_message = rsa_encrypt(message, server_public_key)

    # Sign the message with client's private key
    signature = generate_signature(message, private_key)

    # Send encrypted message and signature
    client_socket.sendall(str(encrypted_message).encode())
    client_socket.sendall(str(signature).encode())

    # Receive server's response
    response = client_socket.recv(4096).decode()
    print("\nServer Response:", response)

    client_socket.close()

if __name__ == "__main__":
    start_client()
