#coding=utf8
# auther:shixingjian  time:2020/07/15
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.vmall.com/')
# title_eles = driver.find_elements_by_xpath('//ol[@class]/li')#标签元素列表
# for title_ele in title_eles:
#     print(title_ele.find_element_by_xpath('./div[1]').text)#打印每个标签文本
#     ActionChains(driver).move_to_element(title_ele).perform()#鼠标悬浮
#     se_eles = title_ele.find_elements_by_xpath('./div[2]//span')#二级标签元素列表
#     for se_ele in se_eles:#循环并打印二级便签文本
#         print("\t",se_ele.text)




