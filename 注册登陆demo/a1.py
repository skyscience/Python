import 
import hashlib


def login():
    name = input('请输入用户名')
    pwd = input('请输入密码')
    pwd = doPwd(pwd)

    ip = '10.114.26.218'
    user = 'root'
    passwd = '123456'
    database = 'test'
    charset = 'utf8'
    contact_1 = contact.mc(ip,user,passwd,database,charset)
    contact_1.ct()

    sql = 'select * from user where name=%s and pwd=%s'
    par = [name,pwd]

    
    data = contact_1.fetchone(sql,par)
    if data:
        print('登陆成功')
    else:
        print('登陆失败')


def register():
    name = input('请输入新用户名')
    pwd = input('请输入密码')
    pwd = doPwd(pwd)
    ip = '10.114.26.218'
    user = 'root'
    passwd = '18201423398Hh'
    database = 'test'
    charset = 'utf8'
    contact_1 = contact.mc(ip,user,passwd,database,charset)
    contact_1.ct()
    sql = 'insert into user(name,pwd) values(%s,%s)'
    par = [name,pwd]

    count = contact_1.insert(sql,par)

    if count:
        print('操作成功')
    else:
        print('操作失败')


def doPwd(pwd):
    s1 = hashlib.sha1()
    s1.update(pwd.encode('utf-8'))
    pwd = s1.hexdigest()
    return pwd


print('1.注册    2.登陆')
L = input('请选择')
if L == '1':
    register()
elif L =='2':
    login()
else:
    print('error')
