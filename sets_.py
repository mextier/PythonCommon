#https://itproger.com/course/python/11

#set
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


fib_numbers = set([1, 1, 2, 3, 5, 8, 13, 21])
prime_numbers = set([2, 3, 5, 7, 11, 13, 17, 19])
union = fib_numbers | prime_numbers
intersection = fib_numbers & prime_numbers
difference = fib_numbers - prime_numbers
symmetric_difference = fib_numbers ^ prime_numbers

#frozen set
s = frozenset({10,20,30})
if type(s) is frozenset:
    print("Yes, it's a frozenset.")
print(s)
