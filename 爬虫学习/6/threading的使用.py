import threading
import requests
import time

def get_data(url):
    time.sleep(2)
    response = requests.get(url)
    if response.status_code == 200:
        print('请求成功')


def main():
    start = time.time()
    # for i in range(0,10):
    #     get_data('https://www.baidu.com')
   
    thread_list = []
    for i in range(0,10):
        # (self, group=None, target=None, name=None,
        #          args=(), kwargs=None, *, daemon=None)
        thread = threading.Thread(target=get_data,name='线程'+str(i),args=('https://www.baidu.com',))
        thread_list.append(thread)

    for thread in thread_list:
        # setDaemon(True)表示后台线程，无论子线程是否结束
        # ，只要主线程结束了，所有的子线程都要结束

        #Daemon默认是False：表示设置线程守护，无论主线程是否结束，
        #子线程都会执行内部任务
        # thread.setDaemon(True)
        thread.setDaemon(True)
        thread.start()
    
    #前台线程：告诉主线程，必须要等子线程执行完毕，才能结束
    for thraed in thread_list:
        thraed.join()

    end = time.time()
    print(threading.current_thread().name)
    print(end-start)

if __name__ == '__main__':
    main()