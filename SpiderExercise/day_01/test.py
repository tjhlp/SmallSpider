import time
import threading


def task1():
    print('线程1开始')
    time.sleep(2)
    print('线程1结束')


def task2():
    print('线程2开始')
    time.sleep(3)
    print('线程2结束')


th1 = threading.Thread(target=task1)
th2 = threading.Thread(target=task2)
th1.start()
th2.start()
th1.join()
print('主线程结束')

