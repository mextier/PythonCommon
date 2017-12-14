#Length
print("#Length")
str1 = "123"
print(len(str1))
print('-'*20)


#F-string
print("#F-string")
print(f"list:{[1,2,3]}  set:{{1,2,3}}  tuple:{(1,2,3)}")
print('-'*20)


#StartsWith EndsWith
print("#StartsWith EndsWith")
str = "python.help.class"
if str.startswith('python'):
	print("starts with python\n")
if str.endswith('class'):
	print("ends with class\n")
print('-'*20)


#String to list of chars
print("#String to list of chars")
str1 = "1234567890"
l1 = list(str1)
print(l1)
print('-'*20)

#Join
print("#Join")
l = ['E','X','A','M','P','L',"E"]
s = ','.join(l)
print(s)
print('-'*20)


#Split
print("#Split")
for s in str.split('.'):
	print(s)
s="S.P.L.I.T."
l=list(c for c in s.split('.') if c!='')
print(l)
print('-'*20)


#Empty string
print("#Empty string")
str= None
if not str:
	print("str is empty\n")
print('-'*20)

#Reverse
print("#Reverse")
s = "String is here!"
s=list(reversed(s))
print(s)
print('-'*20)

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
