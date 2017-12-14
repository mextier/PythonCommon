a = { 1, 2, 3}
b = {3,4,5}

print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))

print (a.union(b))
print(a.intersection(b))



print(a.union({678}).union({11}))
newlist = list(a)
print('newlist is {}'.format(newlist))


newset = set(range(1,11))
print(newset)

