



t = (10,20,30)
print(dir(t))
print(iter([1,2,3]))
#print([*iter[1,2,3]])

print(hash(t))
print(t[1])



class BankAccount:
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name



a1=BankAccount('Dmitriy')
print(a1)

print(hash(a1))






#factorial starts
n = 7

from math import factorial as fact
a=input(f"Standart math:{fact(n)}")

from functools import reduce
fn=reduce(lambda x,y:x*y, range(1,n+1))
a=input(f"Via reduce:{fn}")

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
a=input(f"Recursion:{fact(n)}")

def facte(n):
    if not isinstance(n,int) or n < 1:
        raise Exception("Argument must be int >= 1")
    def __f(n):
        if n == 1:
            return 1
        else:
            return(n*__f(n-1))
    return __f(n)
a=input(f"Recursion with Exception:{facte(n)}")


def factg(n):
    f, i = 1, 1
    while i <= n:
        f = f * i
        yield (i , f)
        i += 1
for _ in factg(n):
    print(_)
a=input(f"Through generator:{_}")
#factorial ends


def gettr(data):
    rList=[]
    for i,item in enumerate(data):
        rList.append(item)
        if (i+1) % 3 == 0 or i==len(data)-1:
            yield tuple(rList)
            rList.clear()



for t in gettr([i for i in range(20)]):
    print(t)




s = sum(int(s) for s in (str(2**1000)))
print(s)




def db(**oldlocals):
    print(f"{a} {b}")
    print(oldlocals)
    print(locals())



a=1
b=2
#type db(**locals())
#breakpoint()
print(12)

#найти не парный
d = [1,2,2,1,5,3,3,7,5] #7
s = int(0)
for item in d:
    s = s ^ item
print(s)





#
from collections import Counter
c = Counter([1,1,2,3,4,4,5,5,5,5])
print(c)
s = [el for el,data in c.items() if data==1]
print(s)
print(sum([i for i in range(5)]))
