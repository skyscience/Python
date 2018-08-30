# 安装pip install psutil
import psutil
import time


print('CPU线程数:',psutil.cpu_count())
print('CPU核心数:',psutil.cpu_count(logical=False))
print('用户登陆信息:',psutil.users())
print('磁盘分区信息:',psutil.disk_partitions())
print('磁盘总大小:',psutil.disk_usage('C:/').total/1024/1024/1024)  


while 1:
    # CPU内存利用率===========
    print('内存利用率',psutil.virtual_memory().percent)
    print('CPU利用率',psutil.cpu_percent(None))
    print('CPU各个核心利用率',psutil.cpu_percent(percpu=True))


    # 内存的===========
    mem = psutil.virtual_memory() #内存
    print('系统总计内存:',mem.total/1024/1024)
    print('已使用内存',mem.used/1024/1024)
    print('空闲内存',mem.free/1024/1024)


    # SWAP内存的=======
    smem = psutil.swap_memory() #SWAP交换分区内存
    print('swap系统总计内存:',smem.total/1024/1024)
    print('swap已使用内存',smem.used/1024/1024)
    print('swap空闲内存',smem.free/1024/1024)
    

    # 磁盘读写的==========
    rwdisk = psutil.disk_io_counters()
    print('读取总数:',rwdisk.read_count/1024/1024)
    print('写入总数:',rwdisk.write_count/1024/1024)
    print('读取kb:',rwdisk.read_bytes/1024/1024)
    print('写入kb:',rwdisk.write_bytes/1024/1024)
    print('读取时间:',rwdisk.read_time)
    print('写入时间:',rwdisk.write_time)


    # 网络=============
    net = psutil.net_io_counters()
    print('发送kb数:',net.bytes_sent/1024)
    print('接收kb数',net.bytes_recv/1024)


    # 磁盘的===========
    disk = psutil.disk_usage('C:/')#Linux 改为'/'
    print('磁盘已用大小:',disk.used)
    print('磁盘剩余空间:',disk.free)
    print('磁盘率:',disk.percent)
    time.sleep(1)




# 网络信息与磁盘IO信息类似,涉及到几个关键点，包括byes_sent(发送字节数),byte_recv=xxx(接受字节数),
# pack-ets_sent=xxx(发送字节数),pack-ets_recv=xxx(接收数据包数),这些网络信息用
# print('网络每个接口信息:',psutil.net_io_counters(pernic=True))



# print('系统全部进程:',psutil.pids())
# 单个进程
# p = psutil.Process(2304)
# print('进程名:',p.name())
# psutil.test()  #模拟ps
"""
p.name()   #进程名
p.exe()    #进程的bin路径
p.cwd()    #进程的工作目录绝对路径
p.status()   #进程状态
p.create_time()  #进程创建时间
p.uids()    #进程uid信息
p.gids()    #进程的gid信息
p.cpu_times()   #进程的cpu时间信息,包括user,system两个cpu信息
p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
p.memory_percent()  #进程内存利用率
p.memory_info()    #进程内存rss,vms信息
p.io_counters()    #进程的IO信息,包括读写IO数字及参数
p.connectios()   #返回进程列表
p.num_threads()  #进程开启的线程数
"""