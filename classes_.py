class Papa:
	pass


p = Papa()
p.name= 'Pope'
p.age = 70
print(p.name,p.age)
print(type(p))




class User:
	def __init__(self,name,age):
		self.name = name
		self.age = age



u = User('Dmitry',88)

print(f"Name:{u.name} Age:{u.age}")



name_ = getattr(u,"name")
age_ = getattr(u,"age")
print(name_,age_)
if hasattr(u,"name"):
	print('u has got attr "name"')
#setattr
#delattr




#ермак
#№Суммы по бл за счет фсс, беременности и родам , не входят в всего начислено.
