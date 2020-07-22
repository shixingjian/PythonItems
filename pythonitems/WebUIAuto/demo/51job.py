#coding=utf8
# auther:shixingjian  time:2020/07/13
from selenium import webdriver
from time import sleep
import xlwt
workBook = xlwt.Workbook()
workSheet = workBook.add_sheet('51job')
driver = webdriver.Chrome()
driver.get('https://51job.com')
driver.find_element_by_css_selector('#kwdselectid').send_keys('python')#搜索框输入python
driver.find_element_by_css_selector('.ush > button:nth-child(2)').click()#点击搜索
driver.find_element_by_css_selector('#work_position_click > p:nth-child(1)').click()#点击选择地区
sleep(1)
addr_ele = driver.find_element_by_css_selector('#work_position_click_multiple_selected')#已选地区栏
addr_eles = addr_ele.find_elements_by_class_name('ttag')#已选地区元素列表
hz_ele = driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200')#杭州地区元素
if len(addr_eles) != 0:#判断是否已选中地区
    for one in addr_eles:
        one.find_element_by_tag_name('span').click()#点击已选地区
    hz_ele.click()#点击确认杭州
else:
    hz_ele.click()
driver.find_element_by_id('work_position_click_bottom_save').click()#点击确认地区
driver.find_element_by_css_selector('button.p_but').click()#点击搜索
sleep(1)
#获取职位表
page_num = int(driver.find_element_by_css_selector('span.td:nth-child(3)').text[1:3])
row = 0
for i in range(1,page_num+1):
    print('-'*10,f'这是第{i}页','-'*10)
    table_job = driver.find_element_by_id('resultList')#job信息表元素
    joblist = table_job.find_elements_by_class_name('el')#工作行列表
    for job in joblist:
        # if 'title' in job.get_attribute('class'):#去掉首行
        #     continue
        jobinfos = job.find_elements_by_tag_name('span')#工作信息行每项元素
        workSheet.write(row,0,jobinfos[0].text)
        workSheet.write(row,1,jobinfos[1].text)
        workSheet.write(row,2,jobinfos[2].text)
        workSheet.write(row,3,jobinfos[3].text)
        row += 1
    if i == 3:
        break
        # for one in jobinfos:
        #     print(one.text,end=' | ')
        # print()
    driver.find_element_by_link_text('下一页').click()
workBook.save('../data/job.xls')


# driver.quit()
