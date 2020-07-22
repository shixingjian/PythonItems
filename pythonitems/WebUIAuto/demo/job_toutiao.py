#coding=utf8
# auther:shixingjian  time:2020/07/13
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get('https://www.toutiao.com')
driver.maximize_window()
ele_list = WebDriverWait(driver,5,0.5).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'channel')))
# ele_list = driver.find_elements_by_class_name('channel')#获取列表
ele_more = ele_list[-1].find_elements_by_tag_name('li')[12]#更多按钮元素
ActionChains(driver).move_to_element(ele_more).perform()#鼠标悬浮在更多上
morelist = ele_more.find_elements_by_class_name('bui-left')
for one in morelist:
    print(one.find_element_by_tag_name('span').text)


# driver.maximize_window()
# more_ele = driver.find_element_by_css_selector('.channel-more')
# ActionChains(driver).move_to_element(more_ele).perform()
# ul_ele = driver.find_element_by_css_selector('.channel > ul:nth-child(2)')
# elelist = ul_ele.find_elements_by_tag_name('span')
# for one in elelist:
#     if one.text != '更多':
#         print(one.text)

sleep(3)
driver.quit()