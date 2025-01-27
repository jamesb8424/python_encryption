import cryptography
import cryptography.hazmat
import cryptography.hazmat.primitives
import cryptography.hazmat.primitives.asymmetric
import cryptography.hazmat.primitives.asymmetric.rsa 

private_key = \
    cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )
print("private_key: ", private_key)
print("private_key actual data: ", private_key.private_bytes())

