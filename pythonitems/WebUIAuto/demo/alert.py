#coding=utf8
# auther:shixingjian  time:2020/07/13
from selenium import webdriver
from time import sleep
import pytest
driver = webdriver.Chrome();
driver.get(r'F:\pythonitems\WebUIAuto\data\alert.html')
# driver.find_element_by_id('bu1').click()
# al = driver.switch_to.alert#获取对话框对象
# al.accept()#确认

# driver.find_element_by_id('bu2').click()
# al = driver.switch_to.alert#获取对话框对象
# al.accept()#确认
# driver.find_element_by_id('bu2').click()
# al.dismiss()#取消

driver.find_element_by_id('bu3').click()
al = driver.switch_to.alert#获取对话框对象
al.send_keys('nn')#发送文本
al.accept()
sleep(3)
driver.quit()