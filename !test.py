def gettr(data):
    rList=[]
    for i,item in enumerate(data):
        rList.append(item)
        if (i+1) % 3 == 0 or i==len(data)-1:
            yield tuple(rList)
            rList.clear()



for t in gettr([i for i in range(20)]):
    print(t)
