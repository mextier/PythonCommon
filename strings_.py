s1=input().lower()
s2=input().lower()
print(set(s1)==set(s2) and len(s1)==len(s2))
input()


#Compare reverse
print("#Compare reverse")
s1=input()
s2=input()
b= s1[:]==''.join(reversed(list(s2)))[:]
b1 = s1[:]==s2[::-1]
print(b)
print(b1)
input()
print('-'*20)

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
