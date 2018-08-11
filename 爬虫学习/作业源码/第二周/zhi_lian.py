import time  #python时间
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor
from mypy import *
from selenium import webdriver
import requests
import csv,os
from lxml import etree
mysqlHelper = MysqlHelper('127.0.0.1','root','1227bing','zhilian')



def get_data(driver):
    print('获取标题')
    title_url_list = []
    for page in range(1,2):
        html = driver.page_source
        csxml = etree.HTML(html)
        bhtml = BeautifulSoup(html,'lxml')

        title_list = bhtml.select('.zwmc div a')
        title_url_list = []
        for titles in title_list:
            title_url = titles.attrs['href']#标题链接
            if title_url != 'http://e.zhaopin.com/products/1/detail.do' and title_url != 'http://xiaoyuan.zhaopin.com/first/':
                title_url_list.append(title_url)
            title = titles.get_text()



        input_list = driver.find_element_by_id('goto')
        input_list.send_keys()
        driver.find_element_by_class_name('next-page').click()
    return pool(title_url_list)


def cs_selenium():
     print('开始操作浏览器!')
   
    optins = webdriver.ChromeOptions()
    optins.set_headless()
    driver = webdriver.Chrome(options=optins,executable_path=r'C:\Users\USMC\Desktop\chromedriver')


    driver.get('https://www.zhaopin.com/')
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('return-to-old').click()
    driver.find_element_by_id('KeyWord_kw2').send_keys(search)
    driver.find_element_by_class_name('doSearch').click()
    get_data(driver)



def parse_data(url):
    url = url.result()
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
    response = requests.get(url,headers=headers)
    html = response.text
    xml = etree.HTML(html)

  
    company_name = xml.xpath('//h1/text()')  #公司名称
    if len(company_name) == 0:
        company_name = '无'
    else:
        company_name = company_name[0].strip()
   
    
    nature = xml.xpath('//table[@class="comTinyDes"]/tr[1]/td[2]/span/text()')#公司性质
    if len(nature) == 0:
        nature = '无'
    else:
        nature = nature[0]
    print(nature)
    


    scale = xml.xpath('//table[@class="comTinyDes"]/tr[2]/td[2]/span/text()')#公司规模
    if len(scale) == 0:
        scale = '无'
    else:
        scale = scale[0]
    #公司行业
    industry = xml.xpath('//table[@class="comTinyDes"]/tr[4]/td[2]/span/text()')
    if len(industry) == 0:
        industry = '无'
    else:
        industry = industry[0]
    #公司地址
    address = xml.xpath('//table[@class="comTinyDes"]//span[@class="comAddress"]/text()')
    if len(address) == 0:
        address = '无'
    else:
        address = address[0]
    
    # #公司网站
    companyUrl = xml.xpath('/html/body/div[2]/div[1]/div[1]/table/tr[3]/td[2]/span/a/@href')
    if len(companyUrl) == 0:
        companyUrl = '无'
    else:
        companyUrl = companyUrl[0]
    #公司介绍
    jieshao = xml.xpath('/html/body/div[2]/div[1]/div[2]/div/p[1]/span/text()')
    recommend = ''
    for i in jieshao:
        a = i.replace('\xa0','')
        recommend+=a
 

    mysqlHelper.connect()   #添加到数据库
    sql = 'insert into companydata values(0,%s,%s,%s,%s,%s,%s,%s)'
    params = [company_name,nature,scale,industry,address,companyUrl,recommend]
    content = mysqlHelper.insert(sql,params)
    if content:
        print('添加数据库成功')
    else:
        print('添加失败')




def request_data(url):
    print('子进程'+str(os.getpid()))
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181'
        }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        html = response.text
    xml = etree.HTML(html)



    #职位
    position = xml.xpath('//h1/text()')[0]
    #公司
    company = xml.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()')[0]
    #职位月薪
    pay = xml.xpath('/html/body/div[6]/div[1]/ul/li[1]/strong/text()')[0]
    #发布时间
    date = xml.xpath('//span[@id="span4freshdate"]/text()')[0]
    #工作经验
    experience = xml.xpath('/html/body/div[6]/div[1]/ul/li[5]/strong/text()')[0]
    #招聘人数
    numbers = xml.xpath('/html/body/div[6]/div[1]/ul/li[7]/strong/text()')[0]
    #工作地点
    address = xml.xpath('/html/body/div[6]/div[1]/ul/li[2]/strong/a/text()')[0]
    #工作性质
    nature = xml.xpath('/html/body/div[6]/div[1]/ul/li[4]/strong/text()')[0]
    #最低学历
    education = xml.xpath('/html/body/div[6]/div[1]/ul/li[6]/strong/text()')[0]
    #职位类别
    cstype = xml.xpath('/html/body/div[6]/div[1]/ul/li[8]/strong/a/text()')[0]
    #岗位职责
    zheze = xml.xpath('/html/body/div[6]/div[1]/div[1]/div/div[1]/p[1]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[2]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[3]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[4]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[5]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[6]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[7]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[8]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[9]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[10]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[11]/text()|/html/body/div[6]/div[1]/div[1]/div/div[1]/p[12]/text()')
    statement=''
    for i in zheze:
    #岗位职责
        statement+=i



    #公司详情接口
    company_url = xml.xpath('//p[@class="company-name-t"]/a[@rel="nofollow"]/@href')[0]
    mysqlHelper = MysqlHelper('127.0.0.1','root','1227bing','zhilian') 
    mysqlHelper.connect()
    sql = 'insert into zhiliandata values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    params = [position,company,pay,date,experience,numbers,address,nature,education,cstype,statement,company_url]
    content = mysqlHelper.insert(sql,params)
    return company_url



def pool(url_list):
    #进程池
    print('开启主进程'+str(os.getpid))
    pool = ProcessPoolExecutor(4)
    for url in url_list:
        handler = pool.submit(request_data,url)
        handler.add_done_callback(parse_data)
    pool.shutdown(wait=True)




search = input('请输入名称或职位: ')
cs_selenium()