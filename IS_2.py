import math

# Input plaintext and key
plaintext = "transposition technique using python"
key = 8

# Encryption
ciphertext = [''] * key
for column in range(key):
    pointer = column
    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]
        pointer += key

cipher = ''.join(ciphertext)  # Removed space to make decryption work correctly
print("Encrypted Text:", cipher)

# Decryption
nC = math.ceil(len(cipher) / key)
nR = key
numOfShadedBoxes = (nC * nR) - len(cipher)

pt = [''] * nC
col = 0
row = 0

for symbol in cipher:
    pt[col] += symbol
    col += 1
    if (col == nC) or (col == nC - 1 and row >= nR - numOfShadedBoxes):
        col = 0
        row += 1

print("Decrypted Text:", ''.join(pt))