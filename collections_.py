#https://docs.python.org/3.3/library/collections.html
#https://pythonworld.ru/moduli/modul-collections.html
#https://www.youtube.com/watch?v=_RxuKNR3VeA
#https://www.youtube.com/watch?v=CZWJT1tm-8g

from collections import OrderedDict, Counter

dict1 = dict()
dict1['Filed2']="value2"
dict1['Field1']="value1"
dict2=OrderedDict(sorted(dict1.items()))
print(dict2)


#from collections import Counter
d = [10,20,30,30,40,50,50,50]
print(Counter(d))
