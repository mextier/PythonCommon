#https://pythonworld.ru/moduli/modul-time.html
#https://python-scripts.com/datetime-time-python

import time



break_time = int(input("Length of break (seconds):"))
work_time = int(input("Length of working time (seconds):"))
while True:
    print("{} You need to start working!".format(time.ctime()))
    time.sleep(work_time)
    print("{} You need to take a break!".format(time.ctime()))
    time.sleep(break_time)
    
    