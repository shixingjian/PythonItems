#coding=utf8
# auther:shixingjian  time:2020/07/13
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import pytest
driver = webdriver.Chrome();
driver.get(r'F:\pythonitems\WebUIAuto\data\demoselect.html')
ele = driver.find_element_by_id('a')
Select(ele).select_by_index(1)#下拉框下标选择
sleep(3)
Select(ele).select_by_value('b')#value选择
sleep(2)
Select(ele).select_by_visible_text('333')#可见文本选择
# Select(ele).deselect_by_index('333')#不选择
sleep(3)
driver.quit()