import os
import sys
from scrapy.cmdline import execute

#设置工程目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#这里我们可以打印出来可以查看输出的是什么，便于理解为什么这么写


print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

#启动爬虫
execute(["scrapy","crawl","tencentJob"])