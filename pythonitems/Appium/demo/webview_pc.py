#coding=utf8
# auther:shixingjian  time:2020/07/17
# ------------在电脑上自动化手机页面，用电脑上的浏览器---------------
from selenium import webdriver
#已手机模式打开浏览器
options = webdriver.ChromeOptions()
options.add_experimental_option(
    "mobileEmulation",
    {"deviceName":"iPhone X"}
)
print(options.to_capabilities())
driver = webdriver.Chrome(desired_capabilities=options.to_capabilities())
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
driver.find_element_by_css_selector('div.con-wrap>input').click()
driver.find_element_by_css_selector('div.con-wrap>input').send_keys('pyhton\n')
input('nnn')
driver.quit()