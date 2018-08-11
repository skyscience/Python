# from queue import Queue
from multiprocessing import Process,Queue
import os,time



a = 0

def main(pageQueue,name):
    # global a
    # a = 3
    # print(a)
    while not pageQueue.empty():

        print(name + str(os.getpid()))
        time.sleep(1)
        page = pageQueue.get()
        print(page)


def run(pageQueue,name):
    print(a)
    while not pageQueue.empty():
        print(name + str(os.getpid()))
        time.sleep(1)
        page = pageQueue.get()
        print(page)


if __name__ == '__main__':

    pageQueue = Queue(50)
    for i in range(0,30):
        pageQueue.put(i)

    # 进程之间数据不共享
    p1 = Process(target=main,args=(pageQueue,'main1'))
    p2 = Process(target=run,args=(pageQueue,'run1'))

    p1.start()
    p2.start()

    print(a)