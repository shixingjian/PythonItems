#coding=utf8
# auther:shixingjian  time:2020/07/17
from Boos.config import Caps,HOST
from appium import webdriver
driver = webdriver.Remote(HOST,Caps.get_Caps())
driver.implicitly_wait(10)
#滑动操作
window_size = driver.get_window_size()#获取屏幕的长宽
width = window_size["width"]
height = window_size['height']
start_x = width/2
start_y = height/8*7
end_x = width/2
jobitem_ele = driver.find_element_by_id('com.hpbr.bosszhipin:id/boss_job_card_view')
distance = jobitem_ele.size['height']#滑动距离为元素高度
driver.implicitly_wait(0)
while True:
    driver.swipe(start_x,start_y,end_x,start_y-distance)#根据滑动的举例确定终点坐标，滑动
    target = driver.find_elements_by_android_uiautomator('new UiSelector().textContains("QA")')
    if target:
        print('找到元素')
        break
driver.implicitly_wait(10)

input(',,,,')
driver.quit()
