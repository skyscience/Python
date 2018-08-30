from django.shortcuts import render
from django.http import request

import datetime
from . import contact



def fk(request):
    # a=request.GET.getlist('a')
    a=request.GET['a'] #ID
    b=request.GET['b']  #联系方式
    c=request.GET['c']  #内容
    print('[建议]:',a,b,c)


    # 传值
    fid = a
    fnow_time = datetime.datetime.now()  #当前时间
    fcontact = b
    fcontent = c




# 连接数据库------------------------------------------------------
    ip = '192.168.1.59'
    user = 'root'
    passwd = '18201423398Hh'
    database = 'web'
    charset = 'utf8'


    
    contact_1 = contact.mc(ip,user,passwd,database,charset)# 实例对象contact_1
    contact_1.ct()  #调用连接函数



#判重------------------------------------------------------
    sql = 'select * from fk_fkinfo where fcontent=%s'
    par = [fcontent]
    data = contact_1.fetchone(sql,par)
    print('data  ==  ',data)
    if data:
        return render(request,'fk/info.html',{'tt':'此内容已被提交过啦!'})
    else:
        print('提交成功!')




# 插入数据----------------------------------------------
    sql = 'insert into fk_fkinfo(fid,fdate,fcontact,fcontent) values(%s,%s,%s,%s)'
    par = [fid,fnow_time,fcontact,fcontent]
    
 
    count = contact_1.insert(sql,par)
    if count:
        print('[信息]:',a,'已提交建议')
    else:
        print('[警告]:',a,'提交失败')

    return render(request,'fk/info.html')
