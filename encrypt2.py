"""
Encrypt a file
"""

from cryptography.fernet import Fernet as F

key = F.generate_key()

with open("../test.py", "rb") as fid:
    data = fid.read()


fernet_object = F(key)
encrypted_data = fernet_object.encrypt(data)

with open("encrypted_test.py", "wb") as fid:
    fid.write(encrypted_data)

with open(".encrypt2_key", "wb") as fid:
    fid.write(key)
    


