#https://pythonworld.ru/moduli/modul-time.html
#https://python-scripts.com/datetime-time-python

import time



break_time = int(input("Length of break (seconds):"))
work_time = int(input("Length of working time (seconds):"))
print("Clock has been started!")
while True:
    time.sleep(work_time)
    print("{} You need to take a break!".format(time.ctime()))
    time.sleep(break_time)
    print("{} You need to start working!".format(time.ctime()))
    