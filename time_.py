#https://pythonworld.ru/moduli/modul-time.html
#https://python-scripts.com/datetime-time-python

import time



break_time = int(input("Length of break (seconds):"))
work_time = int(input("Length of working time (seconds):"))
start_time = time.time()
print("Clock has been started!")
while True:
    if start_time+work_time <= time.time():
        print("{} You need to take a break!".format(time.ctime()))
        start_time = time.time()
    time.sleep(1)
    