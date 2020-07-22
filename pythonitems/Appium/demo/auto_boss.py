# coding=utf8
# auther:shixingjian  time:2020/07/15
# 导包
from appium import webdriver

# 准备自动化配置信息
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

desired_caps = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号,写整数位即可
    'plathformVersion': '6',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息:
    # adb shell dumpsys activity recents | findstr intent={
    'appPackage': 'com.hpbr.bosszhipin',
    'appActivity': '.module.launcher.WelcomeActivity',
    # 'autoGrantPermissions':True#忽略权限
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒
    'newCommandTimeout': 6000,
    # 设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName': 'UiAutomator2',  # 或者UiAutomator1
    'skipServerInstallation': True  # 跳过UI2的安装，如果第一次运行程序，不要添加该配置
}

# 初始化driver对象-用于控制手机-启动被测应用
# IP-appium-server所在机器的网络ip，port-监听的端口号，path固定/wd/hub
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(10)  # 稳定元素
# print(driver.page_source)#获取页面xml
# print(driver.window_handles)#获取窗口
# driver.switch_to.window(driver.window_handles[1])#切换窗口

# 点击放大镜
# driver.find_element_by_xpath(
#     '//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/*').click()  # 先取所有符合条件的元素
WebDriverWait(driver,5,0.5).until(ec.visibility_of_element_located((By.XPATH,'//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/*')),message='超时未找到元素').click()#显式等待
# 搜索框输入职位信息
driver.implicitly_wait(10)
driver.find_element_by_id('et_search').send_keys('软件测试')  # 输入参数
# 选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()

# 获取当前页面所有职位信息元素
job_msg = driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')
for job in job_msg:
    # 输出岗位名称
    name = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
    # print(name.text)
    # 输出薪资
    salray = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
    # print(salray.text)
    # 输出公司名称
    companys = job.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    if companys:
        print('%s|%s|%s' % (name.text, salray.text, companys[0].text))
job_msg[0].click()  # 点击第一个搜索结果
company_addr = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_location').text  # 公司地址
company_years = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_work_exp').text  # 工作年限
company_grades = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_degree').text  # 学历
print(company_addr, ' | ', company_years, ' | ', company_grades)

# input('......')


driver.quit()
