#https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=15

l = [5,3,7,1,4,9]
s_l=sorted(l)
print(s_l)
l.sort(reverse=True)
print(l)

tup1 = (9,3,6,1)
tup2 = sorted(tup1)
print(tup2)

#objects sorting




#Bubble sort
#https://www.youtube.com/watch?v=Ui97-_n5xjo
l = [1,10,2,3,4,7,9,8,5]
for i in range(len(l),1,-1):
	for j in range(i-1):
		if l[j]>l[j+1]:
			l[j] ,l[j+1] = l[j+1], l[j]
print(l)


l = [1,10,2,3,4,7,9,8,5]
Sorted = False
j = len(l)
while not Sorted and j> 0:
	for i in range(j-1):
		if l[i]>l[i+1]:
			l[i] ,l[i+1] = l[i+1], l[i]
			sorted = False
	j -= 1

print(l)