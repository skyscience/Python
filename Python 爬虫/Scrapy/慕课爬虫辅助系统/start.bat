@echo off


echo 1. 获取爬虫数据
echo 2. 启动辅助系统

set /p input=请按照序号选择性输入:
if %input% equ 1 echo a1
    echo [信息]: 爬取数据中...
    d:
    cd D:\Program\Python\Python 爬虫\Scrapy\慕课爬虫辅助系统\mk\mk\spiders
    scrapy crawl mk 


if %input% equ 2 echo a2
    echo [信息]: 辅助系统已启动。
    d:
    cd D:\Program\Python\Python 爬虫\Scrapy\慕课爬虫辅助系统
    python cs.py
@pause
