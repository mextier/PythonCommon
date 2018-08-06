#Rot13
print("#Rot13")
import codecs
strOriginal = "Secret message!"
strEnctypted = codecs.encode(strOriginal,"rot-13")
print(strEnctypted)
strDecryped = codecs.decode(strEnctypted,"rot-13")
strDecrypedMirror = codecs.encode(strEnctypted,"rot-13")
print("Decrypted = {} DecryptedMirror={}".format(strDecryped,strDecrypedMirror))
print('-'*20)

#Caeser Cypher
print("#Caeser Cypher")
shiftNumber = 1
MinNumber = ord('!')
MaxNumber = ord('~')
ExcludeChars  = " "
strOriginal = "Secret message!"
strEncrypted = ""
if shiftNumber<=0:
	raise Exception("Must be greater than 0")
if shiftNumber>100:
	shiftNumber = shiftNumber % 100

for c in strOriginal:
	b = ord(c)
	if c not in ExcludeChars:
		b += shiftNumber
		if b>MaxNumber:
			b=(b-MaxNumber)+MinNumber-1
	strEncrypted += chr(b)
strDecryped = ""
for c in strEncrypted:
	b = ord(c)
	if c not in ExcludeChars:
		b -= shiftNumber
		if b<MinNumber:
			b=MaxNumber - (MinNumber-b) +1
	strDecryped += chr(b)
print("strOriginal={} strEncrypted={} strDecryped={}".format(strOriginal,strEncrypted,strDecryped))
print('-'*20)
