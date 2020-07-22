#coding=utf8
# auther:shixingjian  time:2020/07/11
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://m.weibo.com')
time.sleep(5)
driver.find_element_by_class_name('W_input').click()
elist = driver.find_elements_by_class_name('S_spetxt')#返回元素列表
elist[0].click()
bodylist = driver.find_element_by_xpath('//*[@id="pl_top_realtimehot"]/table/tbody')
rowlist = bodylist.find_elements_by_tag_name('tr')
for row in rowlist:
    tittle = row.find_element_by_tag_name('a').text
    imglist = row.find_element_by_class_name('td-03')
    if imglist.text != '':
        print(tittle,imglist.text)


# driver.get('https://m.weibo.cn')
# time.sleep(3)
# driver.find_element_by_class_name('m-font.m-font-search').click()
# time.sleep(2)
# elist = driver.find_elements_by_class_name('m-link-icon')
# elist[-1].click()
# time.sleep(3)
# rowlist = driver.find_elements_by_class_name('card-list')[0].find_elements_by_class_name('box-left.m-box-col.m-box-center-a')
# for row in rowlist:
#     tittle = row.find_element_by_class_name('main-text.m-text-cut').text
#     imglist = row.find_elements_by_class_name('m-link-icon')
#     if imglist:
#         src = imglist[0].find_element_by_tag_name('img').get_attribute('src')#获取属性src的值
#         if 'hot' in src:
#             print(tittle,'热')
#         elif 'new' in src:
#             print(tittle,'新')
#         elif 'fei' in src:
#             print(tittle,'沸')
#         elif 'recom' in src:
#             print(tittle,'荐')

time.sleep(2)
driver.quit()