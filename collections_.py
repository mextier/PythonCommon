#https://docs.python.org/3.3/library/collections.html
#https://pythonworld.ru/moduli/modul-collections.html

import collections

dict1 = dict()
dict1['Filed2']="value2"
dict1['Field1']="value1"
dict2=collections.OrderedDict(sorted(dict1.items()))
print(dict2)
