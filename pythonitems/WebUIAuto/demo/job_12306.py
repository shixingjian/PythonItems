#coding=utf8
# auther:shixingjian  time:2020/07/14
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
driver.maximize_window()
driver.find_element_by_css_selector('#fromStationText').click()#点击出发地输入框
driver.find_element_by_css_selector('#fromStationText').send_keys('南京南\n')#输入南京南
driver.find_element_by_css_selector('#toStationText').click()#点击目的输入框
driver.find_element_by_css_selector('#toStationText').send_keys('杭州东\n')#输入杭州东
ele = driver.find_element_by_css_selector('#cc_start_time')#选择select
Select(ele).select_by_value('06001200')#选择6-12点
driver.find_element_by_css_selector('#sear-sel>div>ul>li:nth-child(2)').click()#选择后一日
time.sleep(2)
tow_eles=driver.find_elements_by_css_selector('#queryLeftTable>tr>td[colspan="4"]+td+td+td')#每行二等座的元素
train_eles=driver.find_elements_by_css_selector('#queryLeftTable>tr>td[colspan="4"]>div>div>div')#每行车次的元素
for tow_ele,train_ele in zip(tow_eles,train_eles):
    if tow_ele.text == '有':
        print(train_ele.text)
time.sleep(2)
driver.quit()



