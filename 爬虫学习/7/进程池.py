from multiprocessing import Pool
import os,time
def runtest(num):
    print('进程开启'+str(os.getpid()))
    time.sleep(2)
    # print(num)
    print('进程结束'+str(os.getpid()))
    return num,num

def done(future):
    print(future)

#构建一个进程池
p = Pool(4)
for i in range(0,50):
    #func：表示方法（函数）的名称，args：方法（函数）的参数是一个tuple（元组），
    #callback回调函数(不一定要写，看需求)
    p.apply_async(func=runtest,args=(i,),callback=done)

#close()表示关闭进程池，不能再往里面添加任务
p.close()
p.join()


#第一种
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time,os
# #创建一个进程池
# def runtest(num):
#     print('进程开启'+str(os.getpid()))
#     time.sleep(2)
#     # print(num)
#     print('进程结束'+str(os.getpid()))
#     return num

# def done(future):
#     print(future.result())
   
# pool = ProcessPoolExecutor(4)
# for i in range(0,50):
#     handler =  pool.submit(runtest,(i,))
#     handler.add_done_callback(done)

# pool.shutdown(wait=True)







# from multiprocessing import Pool
# import os,time

# def run(num):
#     print('开启进程'+str(os.getpid()))
#     time.sleep(1)
#     print(num)
#     print('关闭进程'+str(os.getpid()))
#     return num

# def done(args):
#     print(args)

# pool = Pool(4)

# for i in range(0,30):
#     pool.apply_async(func=run,args=(i,))

# pool.close()
# pool.join()




