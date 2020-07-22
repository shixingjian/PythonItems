#coding=utf8
# auther:shixingjian  time:2020/07/17
from Boos.config import *
from appium import webdriver
driver = webdriver.Remote(HOST,Caps.get_Caps())
driver.implicitly_wait(10)
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()#点击我的
driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()#点击设置
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()#点击账号与绑定
driver.find_element_by_xpath("//*[@text='修改密码']").click()#点击修改密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys('123')#输入旧密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys('123')#新密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys('')#确认密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()#确认键

input('333')
driver.quit()