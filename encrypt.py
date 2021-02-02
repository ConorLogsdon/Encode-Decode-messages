import cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('secret.key', 'wb') as new_key_file:
    new_key_file.write(key)


############
#print(key)# print your key
############

msg = input("Type message to be encoded: ")

msg = msg.encode()

f = Fernet(key)

ciphertext = f.encrypt(msg)

print(ciphertext)


file = open("test.xml", "wb")
file.write(ciphertext)
file.close()
