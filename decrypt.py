import cryptography
from cryptography.fernet import Fernet

with open('secret.key', 'rb') as privateKey:
    key = privateKey.read()

f = Fernet(key)

ciphertext = open('test.xml', 'rb').read()
cleartext = f.decrypt(ciphertext)
cleartext = cleartext.decode()
print(cleartext)

decoded = open('decoded.txt', 'w')
decoded.write(cleartext)
decoded.close()
