#http://pythonicway.com/education/basics/16-python-lists-intermediate
#https://lancelote.gitbooks.io/intermediate-python/content/book/generators.html

def gen1():
	for i in range(10):
		yield i
l = [i for i in gen1()]
print(l)


def gen2(N):
	for i in range(N):
		yield i

l=[i for i in gen2(5)]
print(l)

g25 = gen2(5)

next(g25) #пропускаем первый эл-нт
while True: #выводим остальные
	try:
		print(next(g25))
	except StopIteration:
		break


str1 = "string here!" #строка - итерируемый объект, но не итератор
str_iter = iter(str1) #берем итератор
for i in range(len(str1)):
	print(next(str_iter))



l = ['Dima','Den','Lena','Andrey']
for i,val in enumerate(l,1):
	print(f'{i}:{val}')

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)



print(dict([(i,j) for i in range(10) for j in range(10,20)]))
