#coding=utf8
# auther:shixingjian  time:2020/07/12
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# -----------------browser--------------------
# driver.maximize_window()#最大化窗口
# driver.minimize_window()#最小化窗口
# driver.set_window_size(900,900)#设置窗口尺寸（宽，高）
# print(driver.find_element_by_id('kw').size)#元素尺寸
# driver.get('http://news.baidu.com/')
# driver.back()#后退
# driver.forward()#前进
# driver.refresh()#刷新
# driver.find_element_by_id('su').text#元素文本值

# -----------------mouse--------------------
# from selenium.webdriver.common.action_chains import ActionChains
# ele = driver.find_element_by_id('s-usersetting-top')
# #perform()执行操作；context_clik()右击；double_click()双击；drag_and_drop()拖动
# ActionChains(driver).move_to_element(ele).perform()#悬停
# driver.find_element_by_class_name('setpref').click()


# -----------------keyboard--------------------
from selenium.webdriver.common.keys import Keys
ele = driver.find_element_by_id('kw')
ele.send_keys("selennium")
#BACK_SPACE删除;SPACE空格;TAB制表键;ESCAPE esc键;ENTER回车;F1..F12;UP上;DOWN下
ele.send_keys(Keys.CONTROL,'a')#全选
sleep(2)
ele.send_keys(Keys.CONTROL,'c')#复制
ele.send_keys(Keys.CONTROL,'v')#粘贴
sleep(3)
driver.quit()


