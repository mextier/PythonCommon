l1 = [10,20,30,40,50]
print(len(l1))



list1 = [10]*5
s = set(list1)
print(list1)
print("-"*20)
print(s)



list2 = [10,'pola',3.1415,[(1,2,3),7,8]]
n,s,f,l = list2
print(l)


listsquares= [i**2 for i in range(1,10)]
print(listsquares)

list3 = [1,2,3,4,5,6,7]
list3b25 = [l5 for l5 in list3 if l5>2 and l5<5]
print(list3b25)


a = [1,2]
b = [3,4]
cortesian_product = [(ai,bi) for ai in a for bi in b]
print(cortesian_product)



l = [1,2,2,3,4,5,5,6,7,7]
l2 = [i for i in l if l.count(i)>1]
print(l2)
