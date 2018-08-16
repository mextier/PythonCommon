#https://docs.python.org/3.3/library/collections.html
#https://pythonworld.ru/moduli/modul-collections.html
#https://www.youtube.com/watch?v=_RxuKNR3VeA
#https://www.youtube.com/watch?v=CZWJT1tm-8g
#https://www.youtube.com/watch?v=GfxJYp9_nJA

#https://www.youtube.com/playlist?list=PLAa4Q914LSAbrPQPGih39Dgp1JKi6SFwH


from collections import OrderedDict, Counter, namedtuple

dict1 = dict()
dict1['Filed2']="value2"
dict1['Field1']="value1"
dict2=OrderedDict(sorted(dict1.items()))
print(dict2)

#from collections import Counter
d = [10,20,30,30,40,50,50,50]
print(Counter(d))



Employee = namedtuple("Employee", ["id", "title", "salary"])
E1 = Employee('A12345', 'Engineer', 100000)
E2 = Employee('A54321', 'Manager', 120000)
print(f"{E1.id} {E1.title} {E1.salary}")
