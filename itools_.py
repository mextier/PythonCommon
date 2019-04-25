#https://pythonworld.ru/moduli/modul-itertools.html
#https://python-scripts.com/itertools
#https://www.youtube.com/watch?v=Qu3dThVy6KQ
#https://www.youtube.com/watch?v=xK7E2YmjyAc

import itertools


for index in range(1,5, 6):
    print(index)

it = itertools.cycle([1,2,'a','b']).__iter__()
for i in range(10):
    print(next(it))


for i in itertools.chain([10,20],list('abc'),('xx','yy','zz')):
    print(i)


for i in list(itertools.compress('ABCDEFG', [True, False, True, True, False])):
    print(i)

things = [("animal", "bear",1), ("animal", "duck"), ("plant", "cactus"),("vehicle", "speed boat"), ("vehicle", "school bus")]
for key, group in itertools.groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
        print('')

l1 = list([i for i in range(10)])
l2= ['First','Second','Third']
l12=list(itertools.zip_longest(l1,l2))
print(l12)