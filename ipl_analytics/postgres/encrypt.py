from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

key = "--enter--key--here--"
password = "--enter--password--here--"

ciphertext = encrypt(key, password)
print(ciphertext)

encoded_ciphertext = b64encode(ciphertext)
print(encoded_ciphertext)

