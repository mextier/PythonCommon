"""
https://www.youtube.com/watch?v=RjMbCUpvIgw
https://www.youtube.com/watch?v=eirjjyP2qcQ
"""


from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time

print(datetime.now())

d = datetime(1970,10,5)
print(d)


orddate=d.toordinal()

print(datetime.fromordinal(orddate))


print("year is "+str(d.year))
print("month is "+str(d.month))
print("day is "+str(d.day))
print("hour is "+str(datetime.now().hour))
print("minute is "+str(datetime.now().minute))
print("second is "+str(datetime.now().second))
print("microsecond is "+str(datetime.now().microsecond))

dstart = datetime.now()
dt = timedelta(100)
dend = dstart + dt
print(dend)


message = "was born on {:%A, %B, %d, %Y}"
print(message.format(datetime(1980,2,26)))



d1 = datetime.now()
d2 = datetime(d1.year+1,2,26)
print(str(d2-d1) + " days left to a birthday")

d = date(2000,1,1)
print(d)
t = time(10,20,0) #hh:mm:ss
print(t)
