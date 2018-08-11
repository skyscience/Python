import urllib.request
# https://httpbin.org/post
#目标url

# http://www.tuniu.com/theme/qinzi/
url = 'http://www.tuniu.com/theme/qinzi/'
response = urllib.request.urlopen(url)
print(response.status)
if response.status == 200:
    # print(response.read())
    htmlContent = response.read().decode('utf-8')
    #w: 如果文件存在，那么我们直接写入必须是字符串，如果之前存在内容，会覆盖
    #wb：如果文件存在，那么我们直接写入必须是字节类型，如果之前存在内容，会覆盖
    #w+：表示文件的读写模式，如果文件存在，那么我们直接写入必须是字符串，如果之前存在内容，会覆盖
    #wb+：表示文件的读写模式，如果文件存在，那么我们直接写入必须是字节类型，如果之前存在内容，会覆盖
    #r：只读
    #a：追加，写入的必须是字符串，每次会在文件末尾追加
    #ab：追加，写入的必须是二进制，每次会在文件末尾追加
    #a+、ab+

    #写入文件的两种方式
    with open('tunian.html','w') as f:
        f.write(htmlContent)
    #方式二
    f = open('tunian.html','w')
    f.write(htmlContent)
    f.close()


