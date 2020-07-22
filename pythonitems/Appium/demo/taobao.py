#coding=utf8
# auther:shixingjian  time:2020/07/17
from appium import webdriver
from Boos.config import *
from time import sleep
driver = webdriver.Remote(HOST,Caps.get_Caps(package_name='com.sina.weibo',activity_name='.SplashActivity'))
driver.implicitly_wait(10)
sleep(5)
win = driver.get_window_size()
print(win['width'],win['height'])
print(driver.contexts)#native/hybird
# driver.switch_to.context("WEBVIEW_com.jingdong.app.mall")#切换context操作
# driver.switch_to.context(driver.contexts[1])#切换context操作
# driver.find_element_by_xpath('//*[@content-desc="我的淘宝"]').click()#点击我的
# driver.find_element_by_xpath('//*[@content-desc="发现"]').click()#点击发现
# driver.find_element_by_xpath('//*[@text="新闻"]').click()#点击
driver.find_element_by_xpath('//*[@content-desc="发现"]').click()#点击发现
driver.find_element_by_xpath('//android.widget.TextView[@text="头条"]').click()#点击头条
print(driver.contexts)
input(",,,")
print(driver.contexts)
input(",,,")
driver.quit()