#combinations	n!/r!/(n-r)!
#permutations	n1/(n-r)!


from itertools import repeat as zzz

for i in zzz(10,3):
	print(i)

from itertools import combinations
from itertools import permutations
from itertools import count

print(len(list(combinations(range(3),2))))
print(len(list(permutations(range(15),4))))


#comb = combinations(range(2),2)
#per = permutations(range(15),4)
#c = sum(1 for _ in comb)
#c = len(list(per))
#print(c)
#print(type(comb))

