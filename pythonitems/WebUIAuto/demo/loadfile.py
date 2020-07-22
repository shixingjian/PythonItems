#coding=utf8
# auther:shixingjian  time:2020/07/13
from selenium import webdriver
from time import sleep
import win32com.client
import pytest
driver = webdriver.Chrome()
# driver.get(r'https://tinypng.com/')
# driver.find_element_by_class_name('icon').click()
# sh = win32com.client.Dispatch('WScript.shell')#创建敲击键盘对象
# sleep(5)
# sh.Sendkeys('''"F:\pythonitems\WebUIAuto\data\\form.png" "F:\pythonitems\WebUIAuto\data\\baidu.png\n"''')
# sleep(10)

# driver.get('http://www.51job.com')
#浏览器滚动条
# driver.execute_script('window.scrollBy(0,100)')#向下移动100像素点
# # driver.execute_script('window.scrollBy(0,-100)')
# # driver.execute_script('window.scrollBy(100,0)')#向右
# # driver.execute_script('window.scrollBy(-100,0)')
#元素滚动条：
driver.get(r'F:\pythonitems\WebUIAuto\data\test.html')
driver.execute_script("document.getElementsByClassName('scroll')[0].scrollLeft=100")#向左
driver.execute_script("document.getElementsByClassName('scroll')[0].scrollDown=100")#向下
sleep(5)
driver.quit()