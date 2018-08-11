#urllib.error: 是处理请求异常，有时候我们在发送请求的时候，会出现没联网、未找到服务器等等原因
#这时候有可能会使代码崩溃，所以我们需要做容错处理

#在urllib.error: urlerror 、httperror（httperror是urlerror的子类）

import urllib.error as error
import urllib.request as request
import ssl

#什么时候会报URLError：我的连接是错误的
1.连不上对应的服务器
2.压根连不上网
3.对方服务器挂掉了
#什么时候会HTTPError：
1.可以连接上服务器，但是请求错误

url = 'https://home.jsbcsbcjksdbckasb.cn/'

try:
    response = request.urlopen(url,context=ssl._create_unverified_context())
except error.HTTPError as err:
    print(err)
    print('HTTPError')
except error.URLError as err:
    print('URLError')
else:
    print('请求成功')