from functools import lru_cache

@lru_cache(maxsize= 500)
def Fiba(num):
	if type(num) != int:
		return 0
	if num<=2:
		return 1
	else:
		return Fiba(num-1) + Fiba(num-2)

for i in range(1,51):
	print(Fiba(i+1)/Fiba(i))

Fiba.cache_clear()
