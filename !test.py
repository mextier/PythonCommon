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
breakpoint()
print(12)
