#https://www.python-course.eu/python3_magic_methods.php
#https://habrahabr.ru/post/186608/
#https://lancelote.gitbooks.io/intermediate-python/content/book/__slots__magic.html

#__dict__

class TestLocals(object):
    def __init__(self, a, b, c, d, e, f=15):
        self.a=a
        print(locals().items())
        #self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

tl = TestLocals(10,11,12,13,14,15)
print("-"*40)
print(tl.__dict__)
