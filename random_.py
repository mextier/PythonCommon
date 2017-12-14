import random

for i in range(10):
	print(random.random()) #[0..1)


print(random.uniform(10,15)) #[10..15]

print(random.normalvariate(0,1)) #normal variation


for i in range(10):
		print(random.choice(["Left","Right","Up","Down"]))


start = (0,0)
(dx,dy) = random.choice([(0,1),(1,0),(-1,0),(0,-1)])
end = (start[0]+dx,start[1]+dy)
print(end)


s1 = {1,2,3}
s2 = s1.union({777})
#print(s1+s2)

l = [10,20,30]
l2= l
l[0]=777
print(l2)

a = 10
b = a
a= 20
print('-'*20)
print(b)


s3 = {1,2,3}
l3 = list(s3)
print("s3 as list {} {}".format(l3[0],l3[1]))


from decimal import *

dec1 = Decimal("10.2")
dec2 = Decimal("5.1")
print(dec1+dec2)
print(getcontext())



