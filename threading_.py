#https://www.youtube.com/watch?v=3lzfxUN8BUI&index=34&list=PLfAlku7WMht6janxhS4D7XqajI7Knq1sS
#https://www.youtube.com/playlist?list=PLV5rPVRE79YikyqHCIrJ33ttjgsXluLVB
#https://docs.python.org/2/library/threading.html
#https://www.youtube.com/watch?v=kKl7scEW90c


import threading
import time


def proca(name):
    time.sleep(5)
    print(f'{name} finished')

for i in range(10):
    t = threading.Thread(target=proca,name=f't{i}',args=(f'thread{i}',))
    t.start()
print('continue...')
