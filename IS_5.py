#Assignment No. 5 – RSA Algorithm Implementation for Encryption and Decryption

import random

# Helper function to calculate the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Helper function to calculate the modular multiplicative inverse
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi

# Function to generate the public and private keys
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    
    # Ensure that gcd(e, phi) = 1
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    # Compute the multiplicative inverse of e (mod phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

# Function to encrypt the plaintext
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

# Function to decrypt the ciphertext
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return (''.join(plain))

if __name__ == '__main__':
    # Input two prime numbers p and q
    p = int(input("Enter a prime number (p>=17): "))
    q = int(input("Enter another prime number (q>=17 & q!=p): "))
    
    # Generate public and private key pairs
    public, private = generate_keypair(p, q)
    
    # Print the generated keys
    print("Public key: ", public)
    print("Private key: ", private)
    
    # Input a message to encrypt
    message = input("Enter a message to encrypt: ")
    
    # Encrypt the message
    encrypted_message = encrypt(public, message)
    print("Encrypted message: ",''.join(map(lambda x: str(x), encrypted_message)))
    
    # Decrypt the message
    decrypted_message = decrypt(private, encrypted_message)
    print("Decrypted message: ",decrypted_message)