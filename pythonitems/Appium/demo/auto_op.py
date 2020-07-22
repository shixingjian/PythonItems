#coding=utf8
# auther:shixingjian  time:2020/07/17
from Boos.config import Caps,HOST
from appium import webdriver
from time import sleep
driver = webdriver.Remote(HOST,Caps.get_Caps())
driver.implicitly_wait(10)
#打开通知栏
# driver.open_notifications()
# #关闭通知栏
# #1.上划2.返回键3.Home
# sleep(2)
# KEYCODE_BACK = 4#返回键
# driver.press_keycode(KEYCODE_BACK)

# KEYCODE_VOLUME_UP = 24#音量增加
# for i in range(5):
#     sleep(1)
#     driver.press_keycode(KEYCODE_VOLUME_UP)
search = driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/ly_menu']/android.widget.RelativeLayout[2]")
search.click()
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search').send_keys('软件测试')#输入参数
KEYCODE_ENTER = 66
# KEYCODE_DEL = 67
# driver.press_keycode(KEYCODE_DEL)
driver.press_keycode(KEYCODE_ENTER)
input(',,,,')
driver.quit()
