#coding=utf8
# auther:shixingjian  time:2020/07/12
from selenium import webdriver
from time import sleep
import pytest
driver = webdriver.Chrome();
# driver.get('http://www.baidu.com')
#-------------隐式等待------------
#一次设置，后边代码生效，等待至元素出现，超时未出现报错，效率低，每个元素都会等待
# driver.implicitly_wait(10)
# 获取当前页标题
# print(driver.title)
# #获取当前页URL
# print(driver.current_url)
# #获取标签对之间的文本
# res = driver.find_element_by_partial_link_text('高考').text
# def test_001():
#     assert res == '高考加油'

#-------------显式等待------------
# 等待元素出现，如果出现不再等待，超时会报错，代码执行效率高
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
driver.get('https://m.weibo.cn')
driver.find_element_by_class_name('m-font.m-font-search').click()
#设置元素等待配置，最多等5秒，轮询时间为0.5秒
ele = WebDriverWait(driver,5,0.5).until(
    #直到元素加载完成
    es.presence_of_element_located(
        #设置元素寻找方案，并传入表达式----》写定位元素的方法
        (By.CSS_SELECTOR,'#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > span > img')))
# ele = WebDriverWait(driver,5,0.5).until(es.presence_of_all_elements_located((By.CLASS_NAME,'m-link-icon')))
ele.click()
# driver.find_element_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > span > img').click()
sleep(3)
driver.quit()

