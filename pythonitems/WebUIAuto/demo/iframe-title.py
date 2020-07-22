#coding=utf8
# auther:shixingjian  time:2020/07/12
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
# -----------------iframe----------------
# driver.get(r'F:\pythonitems\WebUIAuto\demo\test.html')
# #找到iframe元素
# iframe = driver.find_element_by_id('abcd')
# #切入到ifreme
# driver.switch_to.frame(iframe)
# # driver.switch_to_frame()#即将弃用
# # driver.switch_to.default_content()#切回主页面
# #操作iframe内的元素
# driver.find_element_by_id('kw').send_keys('nihao')


# -------------------多标签页切换------------------
from selenium.webdriver.common.by import By
driver.get('http://www.baidu.com')
driver.find_element(By.LINK_TEXT,'高考加油').click()
print(driver.current_window_handle)#获取当前页句柄，资源标识符
headers = driver.window_handles#获得所有句柄
print(headers)#返回列表类型
# driver.switch_to.window(headers[2])
# print(headers[2])
for one in headers:
    driver.switch_to.window(one)#遍历，直到跳转到某个标签页
    if '高考' in driver.title:
        print(one)
        break
driver.find_element_by_css_selector('div.op-gk-topic-tool-item:nth-child(1) > a:nth-child(1)').click()
sleep(5)
driver.quit()
