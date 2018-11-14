#https://lancelote.gitbooks.io/intermediate-python/content/book/debugging.html

a = 1
b = a +5
print(b)




import pdb

def make_bread():
    pdb.set_trace()
    return "У меня нет времени"

print(make_bread())




#breakpoint()
