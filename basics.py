#################################
print("if elif else")
age = 33
if age<5:
	print("malysh")
elif age<12:
	print("malchik")
elif age<20:
	print("yunusha")
elif age<25:
	print("paren")
elif age<30:
	print("pochti muzhik")
elif age==33:
	print("Jesus Christ")
elif age>70:
	print("starec")
elif age>60:
	print("starik")
else:
	print("Muzhik!")

print("\nwhile break continue")
n=1
while n<=100:
	if n==3:
		n+=1
		continue
	print(n)
	if n==5:
		break
	n+=1

#################################
print("\n")
a = b = 10
print(a,b)

a, b = 10 , 20
print(a,b)
print("\n")


#################################
print ("\nif and or not")
if 1==1 or 2==2:
	print("1=1 or 2=2")

if 1==1 and 2==2:
	print("1=1 and 2=2")

if 1==1 and 1!=2:
	print("1=1 and 1!=2")

if 1==1 and not 1==2:
	print("1==1 and not 1==2")


#################################
print("\nfor")
s = "Hello!" #все символы
for l in s:
	print(l, end = " ")
print("\n")
for i in range(5): #01234
	print(i, end = " ")
print("\n")
for i in range(0,20,5): #0 5 10 20
	print(i, end = " ")


#################################
print("\nstrings")

message = "This is message!"
if "T" in message:
	print("T is in message!\n")
print("len of message is ", len(message) , end = "\n")

for i in range(0,len(message)):
	print(message[i], end = " ")
print("\n")
for i in range(-1,-len(message)-1, -1): #теперь наоборот -1 это последний символ -2 предпоследний и т.д.
	print(message[i], end = " ")
print("\n")

print(9//2)
print(-9//2)

a,b = 10,20
a,b= b,a
print('a={} b='.format(a,b))


################################ Complex number
iNum1 = 10+5j
iNum2 = 3+3j
print(iNum1+iNum2)


################################# Formating



supernum = 123
s = 0
for c in str(supernum):
	s += int(c)
print(s)
