import cryptography
import cryptography.fernet

encrypted_message = b'gAAAAABnjtQxm2sofjBgSvVQLU7ZZL4IZ5rQ4rPb1JWWWS7gKrWUf7evhmPNavr3358NjB87NBjOs12W8A4Bpm3atsphu4w324Z05F7-J7p-vxYfu9pFoHE='

with open(".my_super_secret_key", "rb") as fid:
    key = fid.read()


fernet_object = cryptography.fernet.Fernet(key)
decrypted_message = fernet_object.decrypt(encrypted_message)
message = decrypted_message.decode("ascii")
print(message)

