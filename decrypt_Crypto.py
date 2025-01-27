from Crypto.Cipher import AES

ciphertext = b'vR\x88\x17a\xcb^\x05\xb8\xa2\xb0|*\xcb\xdf\xe3<\xa5\xabjR 7\xdc@v\xce*\x88\x9b\xa0"'

with open(".aes_Crypto_key", "rb") as fid:
    key = fid.read()
    
cipher = AES.new(key, AES.MODE_CTR)
plaintext = cipher.decrypt(ciphertext)
plaintext = plaintext.decode("ascii")
print(plaintext)


