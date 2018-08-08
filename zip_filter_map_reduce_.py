#http://pythonicway.com/python-functinal-programming
#https://lancelote.gitbooks.io/intermediate-python/content/book/map_filter.html



#map - применяет функцию к каждому эл-ту
mply = lambda x,y: x*y
print(mply(10,20))

strs = ["1","2","3"]
ints = [int(c) for c in strs]
ints2 = list(map(int,strs))
print(ints)
print(ints2)

mile_distances = [1.0,2.0,5.0,80.0]
kilometer_distances = list(map(lambda x:x*1.6,mile_distances))
print(kilometer_distances)

l1 = [1,2,3]
l2 = [1,0,1]
l3 = list(map(lambda x,y:x*y,l1,l2))
s = sum(list(map(lambda x,y:x*y,l1,l2)))
print(f"Sum of {l3} is {s}")

#filter фильтрует
l = range(10)
l_even = [i for i in l if i % 2==0]
l_even2 = list(filter(lambda x:x%2==0,l))
if l_even[:]==l_even2[:]:
		print("Equal!")



#reduce свертка эл-тов - возвращает один элемент
from functools import reduce
items = [1,2,3,4,5]
sum_all = reduce(lambda x,y: x + y, items)
print(sum_all)
maxel = reduce(lambda x,y: x if x>y else y,items)
print(maxel)

#zip объединяет в кортежи
l = [1,2,3]
c = "ABC"
t = list(zip(l,c))
print(t)
#в словари
names = ['Bob','Helen','John']
scores = [1000,9000,8000]
d = dict(zip(names,scores))
print(d)
