#pip install rsa
#https://stuvel.eu/python-rsa-doc/

import rsa

(pubkey, prkey) = rsa.newkeys(512)


message = 'hello Bob!'.encode('utf8')
crypto = rsa.encrypt(message, pubkey)
decrypto = rsa.decrypt(crypto,prkey)

print("Original message is " + message.decode("utf-8"))
print("Decrypted is " + decrypto.decode("utf-8"))
