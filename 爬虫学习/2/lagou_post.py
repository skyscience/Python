#目标url
#https://www.lagou.com/jobs/positionAjax.json?
#city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false
import urllib.request as request
import urllib.parse as parse
import ssl

def getdata(city):
    parmas = {
        'city':city,
        'needAddtionalResult':'false',
    }
    # 这个时候转完是一个字符串
    parmas = parse.urlencode(parmas,encoding='utf-8')
    #构造一个完整的url
    full_url = 'https://www.lagou.com/jobs/positionAjax.json?'+parmas
    #表单数据
    from_data= {
        'first':'true',
        'pn': '1',
        'kd':'python',
    }

    #1.使用urlencode转成url编码格式，在转换成字节
    from_data = parse.urlencode(from_data).encode('utf-8')
    #构造请求
    #构造headers参数的权重
    #User-Agent：模拟浏览器发送请求
    #Cookie：保存用户信息，为了跟服务器的session做交互
    #Referer：表示你当前的请求是从哪个页面或者说哪个接口跳转过来的
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'JSESSIONID=ABAAABAACEBACDG1A745B0B12374B496DB842345FEC1FCE; user_trace_token=20180704071919-0f1c72ad-cda6-4acd-b271-c623aaa66791; _ga=GA1.2.1874412298.1530659960; LGUID=20180704071920-83af21ce-7f17-11e8-98e3-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530659961; _gat=1; LGSID=20180705102716-eeedbbfe-7ffa-11e8-be79-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E5%258C%2597%25E4%25BA%25AC%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20180705102716-eeedbdc1-7ffa-11e8-be79-525400f775ce; _gid=GA1.2.183195595.1530757636; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530757641; SEARCH_ID=64cba07d4bbd46a1b1d837448b6ffd03',
        # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        # 'X-Requested-With':'XMLHttpRequest',
        # 'X-Anit-Forge-Token':'None',
        'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
    }

    req = request.Request(full_url,headers=headers)
    response = request.urlopen(req,context=ssl._create_unverified_context())
    print(response.status)
    print(response.read().decode('utf-8'))

def main():
    city = input('请输入城市')
    getdata(city)

if __name__ == '__main__':
    main()

#总结：post的请求
#1.寻找post请求的url
#2.寻找form_data表单参数
#3.在发送请求之前，我们要将form_data转为为url编码格式，之后在转换为字节类型
#4.构造请求(注意请求头：请求头中参数的权重顺序如下：'User-Agent'、'cookie'、'Referer')
#5.发起请求（注意如果请求的url是https：我们要设置context忽律未授权的ssl）
#6.接收浏览器返回的响应（响应状态吗、响应体、响应头）
#7.清洗数据，做持久化（文件持久化、数据库持久化）
