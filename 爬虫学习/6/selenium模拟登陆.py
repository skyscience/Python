from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
#无界面加载
optins = webdriver.ChromeOptions()
optins.set_headless()
#设置无界面加载模式
driver = webdriver.Chrome(options=optins,executable_path='/Users/ljh/Desktop/chromedriver')

url = 'https://github.com/login'

# 容错
try:
   driver.get(url)
except TimeoutError as err:
    print(err)
else:
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_id('login_field').send_keys('ljhyigehaoren@sina.com')
        driver.find_element_by_id('password').send_keys('ljh123456')
        driver.find_element_by_name('commit').click()
    except NoSuchElementException as err:
        print(err)

print(driver.get_cookies())
for cookie in driver.get_cookies():
    print(cookie['name'],cookie['value'])
