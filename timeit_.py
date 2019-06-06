import timeit

var1 = timeit.timeit("[sqrt(x) for x in range(10**6)]","from math import sqrt",number=1)
print(var1)

var2 = timeit.timeit("for x in range(10**6): l.append(sqrt(x))","from math import sqrt; l = list()",number=1)
print(var2)

var3 = timeit.timeit("list(map(sqrt,range(10**6)))","from math import sqrt",number=1)
print(var3)
