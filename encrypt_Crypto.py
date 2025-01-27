from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256


key = get_random_bytes(16)
hkey = get_random_bytes(16)
print("key: ", key)


cipher = AES.new(key, AES.MODE_CTR)

message = " Hello World, from Ryan to James"
encoded_message = message.encode("ascii")

ciphertext = cipher.encrypt(encoded_message)
print("ciphertext: ", ciphertext)
print("cipher.nonce: ", cipher.nonce)

hmac = HMAC.new(hkey, digestmod=SHA256)
tag = hmac.update(cipher.nonce + ciphertext).digest()

with open(".aes_Crypto_key", "wb") as fid:
    fid.write(key)
    
with open(".encrypted_message", "wb") as fid:
    fid.write(tag)
    fid.write(cipher.nonce)
    fid.write(ciphertext)

    
