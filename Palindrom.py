s1 = "put it up"
s2 = "stack cats"
s3 = "nope"



def isPalindrom(item):
	itemns=[c for c in item if c!=" "]
	return list(reversed(itemns))[:]==itemns[:]

print(isPalindrom([]))
print(isPalindrom(s2))
print(isPalindrom(s3))


def ispar(i):
	return None


print(ispar(10))