def cla1(*args):
    for p in args:
        print(p)
    pass


def cla2(**kwargs):
    print(kwargs)
    pass



cla1(1,10,20,30)

cla2(param1 =1 , request =2, data={})
#cla2({"param1":10, "request":20})
