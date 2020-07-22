#coding=utf8
# auther:shixingjian  time:2020/07/11
from selenium import webdriver
import time
# 设置 ：忽略正在受自动测试软件的控制
# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
# 实例化 对象
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome()#括号内写chromedriver.exe路径，在python根目录下（即环境变量）可以不写
# 打开网址
driver.get("https://www.baidu.com")
# 通过id元素定位到输入框，输入github
# driver.find_element_by_id("kw").send_keys("粘滞键是什么")#id定位
# # 点击百度一下
# driver.find_element_by_id('su').click()#id定位
# driver.find_element_by_class_name('bg s_btn').click()#class属性定位
# driver.find_element_by_name('bg s_btn').click()#name属性定位
# driver.find_element_by_tag_name('a').click()#标签定位
# driver.find_element_by_link_text('新闻').click()#链接文本定位
# driver.find_element_by_partial_link_text('新').click()#链接文本定位/支持模糊搜索
# element = driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()#xpath
element = driver.find_element_by_css_selector('#su').click()#selector选择器定位

time.sleep(5)
driver.quit()
