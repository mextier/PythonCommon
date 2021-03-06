#https://realpython.com/python-string-formatting/
#https://habr.com/post/236633/
#https://docs.python.org/3/library/string.html

#Old style
print("Hello, %s" % "User")
print("Hello %s, I'm %s" % ("User","PC"))
print("Hey %(username)s, what do you want from %(myname)s?" % {"username":"User", "myname":"PC"})
print("Hex value of %d is  %x" % (255,255))
print('*'*50)

#New style formatting
print("Hello, {}".format("Username"))
print("Hello, {param1}".format(param1="Username"))

params = {"userame":"User","myname":"PC"}
print("username is {userame}, but my name is {myname}".format_map(params))

person = {'first':'Reuven', 'last':'Lerner'}
print("Good {0}, {first} {last}".format('morning', **person))
print('*'*50)

#String Interpolation / f-Strings (Python 3.6+)
userame,myname = ("Username","PC")
print(f"username is {userame}, but my name is {myname}")
print('*'*50)

#Template Strings
from string import Template
t = Template("Hey, $username! I'm $myname")
print(t.substitute(username="user",myname="PC"))
print('*'*50)

#Own format
class C(object):
	foo = 1
	def __format__(self, spec):
		if spec == 'of':
			return 'format done'
		else:
			return str(self.foo)
c = C()
print("{}, {:of}".format(c,c))
print('*'*50)

print('Sum\tNDS\tValue')
print('-'*50)
for item in [10,50,100]:
	for nds in (10,18,20):
		print ('{0:d}\t{0:d}\t{1:f}'.format(item,nds,nds*item*(100+nds)/100))
