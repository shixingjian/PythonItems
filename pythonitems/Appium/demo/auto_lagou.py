# coding=utf8
# auther:shixingjian  time:2020/07/16
# 导包
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# 准备自动化配置信息
desired_caps = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号
    'plathformVersion': '6',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息
    'appPackage': 'com.alpha.lagouapk',
    'appActivity': '.HelloActivity',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒
    'newCommandTimeout': 6000,
    # 更换底层驱动
    'automationName': 'UiAutomator2',
    # 'unicodeKeyboard':True,#修改手机的输入法，UI2不需要设置
    # 'resetKeyboard':True#自动化结束之后将输入法还原
}

# 初始化driver对象-用于控制手机
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 稳定元素

# 点击输入框
# driver.find_element_by_id('com.alpha.lagouapk:id/search_tab_txt').click()
# 计算屏幕高度和宽度
win_size = driver.get_window_size()
width = win_size['width']
height = win_size['height']
# 通过坐标点击输入框
sleep(3)
driver.tap([(width / 2, height / 16)])
# 操作输入框-输入职位信息
driver.find_element_by_id('com.alpha.lagouapk:id/result_Search').send_keys('软件测试')
# 点击第一个搜索结果
# res=driver.find_elements_by_id('com.alpha.lagouapk:id/suggest_ps_adpter')
# res[0].click()
KEYCODE_ENTER = 66
driver.press_keycode(KEYCODE_ENTER)
# 查看结果
jobs = driver.find_elements_by_id('com.alpha.lagouapk:id/position_card_content_layout')

for job in jobs:
    job_name = job.find_element_by_id('com.alpha.lagouapk:id/position_name').text
    job_salary = job.find_element_by_id('com.alpha.lagouapk:id/position_card_salary').text
    job_companys = job.find_elements_by_id('com.alpha.lagouapk:id/position_card_company_name')
    if job_companys:
        print(f'{job_name}|{job_salary}|{job_companys[0].text}')

# input('......')


driver.quit()
