import threading
import time

def run():
    time.sleep(2)  #睡眠2秒
    print("\t>_"+threading.current_thread().name)
    time.sleep(2)  



start_time = time.time()
thread_list = []



# 创建线程 加入队列
for i in range(5):
    t = threading.Thread(target=run,name=('线程'+str(i)))
    thread_list.append(t)

# 不避开其它线程
    # for i in range(5):
    #     run()



# 关键点是    我们的计时是针对主线程的，主线程结束他也结束，打印出来的是主线程的。
# 子线程的任务完成之后，主线程随之结束，子线程继续执行自己的任务，
# 直到全部的子线程的任务全部结束，程序结束。




# 可以很明显的看到，主线程结束以后，子线程还没有来得及执行，整个程序就推出了
for thread in thread_list:
    # 设置是否随着主线程终止而结束
    # 请确保setDaemon()在start()之前
    thread.setDaemon(True) #设置线程守护
    thread.start()

# 可以看到，主线程一直等待全部的子线程结束之后，主线程自身才结束，程序退出
for thread in thread_list:
    # 将子线程加入主线程
    thread.join()


print('jc3',threading.current_thread().name)
print('jc2',time.time() - start_time)