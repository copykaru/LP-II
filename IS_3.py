#Assignment No. 3 – DES Encryption/Decryption 

# Import DES module from pycryptodome
from Crypto.Cipher import DES

# Function to pad text to make it multiple of 8 bytes
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

# Function to unpad the decrypted text (removes trailing spaces)
def unpad(text):
    return text.rstrip(b' ')

# Define 8-byte key and plaintext
key = b'hello123'                # 8 bytes = 64 bits (used as 56-bit in DES)
plaintext = b'Python is great'   # Example text

# Pad the plaintext to be a multiple of 8 bytes
padded_text = pad(plaintext)

# Create DES cipher object in ECB mode
des = DES.new(key, DES.MODE_ECB)

# Encrypt the padded plaintext
ciphertext = des.encrypt(padded_text)

# Decrypt the ciphertext
decrypted_text = des.decrypt(ciphertext)

# Remove the padding from decrypted text
decrypted_text = unpad(decrypted_text)

# Display results
print("Original Text   :", plaintext)
print("Encrypted (Hex) :", ciphertext.hex())
print("Decrypted Text  :", decrypted_text)