tup1 = (12, 34.56)
tup2 = ('new tuple', 777)
tup3 = (10,)
print(tup1+tup2)
print(tup1+tup3)

l510 = list([5]*10)
print(l510)

tup510 = (5,)*10
lt510 = list(tup510)
print(lt510)

print(ascii(tup1))



tp1 = (10,20)
tp2 = (30,)
list1 = list(tp1 + tp2)
tp3 = tuple(list1[1:])
print(tp3)


#unpacking
tup1 = (1,2,3)
a,b,c = tup1
print(a,b,c,sep='|')

#packing
a,b,c = 10,20,30
tup2=(a,b,c)
print(tup2)