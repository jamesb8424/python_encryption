"""
The goal is to encrypt a message and then encryot a file
"""

import cryptography
import cryptography.fernet

# AES-256 symmetric key
key = cryptography.fernet.Fernet.generate_key()
print("key: ", key) 

fernet_object = cryptography.fernet.Fernet(key)
message = "hello world, from Ryan to James"

encoded_message = message.encode("ascii")

encrypted_message = fernet_object.encrypt(encoded_message)
print(encrypted_message)

with open(".my_super_secret_key", "wb") as fid:
    fid.write(key)
    

