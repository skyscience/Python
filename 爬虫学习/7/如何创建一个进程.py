from multiprocessing  import Process
import os,time
def run(name):
    time.sleep(5)
    print(name + str(os.getpid()))
    # while True:
    #     print(name + str(os.getpid()))
    #     print('this is run')

def main(name):
    time.sleep(5)
    print(name + str(os.getpid()))
    # while True:
    #     print(name + str(os.getpid()))
    #     print('this is main')
    

if __name__ == '__main__':
    print('主进程开启')

    p1 = Process(target=run,args=('run1',))
    p2 = Process(target=main,args=('main1',))

    # daemon:默认是False：无论主进程是否结束，
    # 我的子进程都会继续执行

    # daemon = True：表式同生共死（主进程结束，子进程也结束）
    # p1.daemon = True
    # p2.daemon = True
    p1.start()
    p2.start()

    #join():告诉主进程，必须等子进程结束才结束。
    p1.join()
    p2.join()
    
    # run()
    # main()
    print('主进程结束')
    