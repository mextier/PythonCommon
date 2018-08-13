#https://realpython.com/python-dicts/

s2 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
s1 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}


names = ['d','o','p']
values = [10,20,30]

print([k for k in s2.keys()])
print(dict(zip(names,values)))

s3=dict(s2)
s3.update(s1)
print(s3)


#merge two dicts Python 3.5+
d1 = {'a':1,'b':2}
d2 = {'a':2,'b':3,'c':10}
merged_dict = {**d1,**d2}
print(merged_dict)
