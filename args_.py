def cla1(*args):
    for i,p in enumerate(args):
        print(i,p)

def cla2(**kwargs):
    print(kwargs)


cla1(1,10,20,30)
print('*'*50)
cla1(1,*"abcd")
print('*'*50)
cla1(1,*[5,6,1,2,18])
print('*'*50)

cla2(param1 =1 , request =2, data={})
print('*'*50)
cla2(text="as")
print('*'*50)




d = {}
param1=10
param2=20



d["param1"]=1
d["param2"]=2
#cla1(**d)
breakpoint()



a=10
b=20
print("{a} {b}".format(**locals()))