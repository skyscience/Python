import urllib.request
import urllib.parse
import ssl
# https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E7%AE%80%E4%B9%A6&rsv_pq=dd7b01c30001385b&rsv_t=1ddbHPrUP5WQQQ%2BsLcZ%2FgnVV0D9GjLQLCypK%2FnLXah1oW1XDFeNNvW1YVFs&rqlang=cn&rsv_enter=1&rsv_sug3=8&rsv_sug1=7&rsv_sug7=101&rsv_sug2=1&prefixsug=jianshu&rsp=0&inputT=2691&rsv_sug4=3840&rsv_jmp=fail

# content = input('请输入你要输入的内容')

# dict = {
#     'wd':content
# }

# dict2 = {
#     'oq':content
# }

# # urlencode query参数：传入的是一个dict，encoding编码的格式（编码的类型）
# # urlencode作用：
# # 1.将咱们传入的字典里面的字符传，重新编码为utf-8的编码，
# # 2将字典的键和值进行了拼接拼接的格式：key（参数）= value（参数值的形式）& key（参数）= value（参数值的形式
# p = urllib.parse.urlencode(query=dict,encoding='utf-8')

# print(p)
# print(type(p))

# p2 = urllib.parse.urlencode(query=dict2,encoding='utf-8')

# # context = ssl._create_unverified_context()

# for pn in range(0,30,10):

#     pn = str(pn)

#     url = 'http://www.baidu.com/s?'+ p + '&pn='+pn+'&' + p2 + '&ie=utf-8&rsv_idx=1&rsv_pq=8412768c0001bf3a&rsv_t=6333sOFUCM75Psomg5kGOwpFEARRKdN%2BOELGX13bQT%2Bi%2BG7LLiWIcXAPyUM'

#     h = urllib.request.urlopen(url)

#     response = h.read().decode('utf-8')

#     f = open(pn+'.html','w')
#     f.write(response)
#     f.close() 

def getdata_from_parmas(parmas):
    full_url = 'https://www.baidu.com/baidu?' + parmas
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    #忽略未认证的ssl
    context = ssl._create_unverified_context()
    #构造了一个请求
    req = urllib.request.Request(full_url,headers=headers)
    #发起请求，接收响应
    response = urllib.request.urlopen(req,context=context)
    print(response.status) #获取请求的状态码
    if response.status == 200:
        #unquote这个方法将我们url编码格式的参数，转换为中文
        filename = urllib.parse.unquote(parmas)
        print(filename)
        file_path = 'baidu/'+filename
        content = response.read().decode('utf-8')
        with open(file_path,'w') as f:
            f.write(content)




def main():
    #设置搜索关键字
    kw = input('请输入搜索关键字：')
    startpage = int(input('输入你要获取的起始页码'))
    endpage= int(input('输入你要获取的截止页码'))
    # https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%93%B6%E9%85%92%E8%8A%82&pn=0
    # https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%93%B6%E9%85%92%E8%8A%82&pn=10
    for i in range(startpage,endpage+1):
        data = {
            'wd':kw,
            'pn':(i-1)*10
        }

        data = urllib.parse.urlencode(data,encoding='utf-8')
        print(data)

        getdata_from_parmas(data)

if __name__ == '__main__':
    main()
