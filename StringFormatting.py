#https://realpython.com/python-string-formatting/

#Old style
print("Hello, %s" % "User")
print("Hello %s, I'm %s" % ("User","PC"))
print("Hey %(username)s, what do you want from %(myname)s?" % {"username":"User", "myname":"PC"})
print("Hex value of %d is  %x" % (255,255))
print('*'*50)

#New style formatting
print("Hello, {}".format("Username"))

print('*'*50)

#String Interpolation / f-Strings (Python 3.6+)
userame,myname = ("Username","PC")
print(f"username is {userame}, but my name is {myname}")

print('*'*50)

#Template Strings
from string import Template
t = Template("Hey, $username! I'm $myname")
print(t.substitute(username="user",myname="PC"))
