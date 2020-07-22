#coding=utf8
# auther:shixingjian  time:2020/07/15
#导包
from appium import webdriver
from Boos.config import Caps

#初始化driver对象-用于控制手机-启动被测应用
#IP-appium-server所在机器的网络ip，port-监听的端口号，path固定/wd/hub
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',Caps.get_Caps())
driver.implicitly_wait(10)#稳定元素

#点击放大镜
eles=driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')#先取所有符合条件的元素
#找到第二个元素--放大镜
btn=eles[1]
btn.click()

#搜索框输入职位信息
search_input=driver.find_element('id','com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')#输入参数

#选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()


#获取当前页面所有职位信息元素
job_msg=driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')
for job in job_msg:
    #输出岗位名称
    name=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
    # print(name.text)
    #输出薪资
    salray=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
    # print(salray.text)
    #输出公司名称
    companys=job.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    if companys:
        print('%s|%s|%s'%(name.text,salray.text,companys[0].text))
job_msg[0].click()#点击第一个搜索结果
company_addr = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_location').text#公司地址
company_years = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_work_exp').text#工作年限
company_grades = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_degree').text#学历
print(company_addr,' | ',company_years,' | ',company_grades)


# input('......')


driver.quit()