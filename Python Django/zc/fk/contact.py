import pymysql

class mc:
    # 定义传入数据库连接信息
    def __init__(self,HOST,USER,PASSWD,DB,CHARSET):
        self.host = HOST
        self.user = USER
        self.passwd = PASSWD
        self.database = DB
        self.charset = CHARSET


# 数据库连接函数
    def ct(self):
        self.contact = pymysql.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                database = self.database,
                charset = self.charset)
        self.tool = self.contact.cursor()



# 查询 匹配状态
    def fetchone(self,sql,params=None):
        dataOne = None
        try:
            count = self.tool.execute(sql,params)
            if count != 0:
                dataOne = self.tool.fetchone()
        except Exception as ex:
            print('[错误] ',ex)
        finally:
            return dataOne


# 插入状态
    def insert(self,sql,par=None):
        return self.__item(sql,par)
    def __item(self,sql,params=None):
        count = 0
        try:
            count = self.tool.execute(sql,params)
            self.contact.commit()
        except Exception as ex:
            print('[Error] ',ex)
        finally:
            self.close()
            return count



# 关闭连接
    def close(self):
        print('数据库链接关闭!')
        if self.tool != None:
            self.tool.close()
        if self.contact != None:
            self.contact.close()