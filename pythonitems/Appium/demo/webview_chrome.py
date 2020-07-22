#coding=utf8
# auther:shixingjian  time:2020/07/17
# ------------在电脑上自动化手机页面，用电脑上的浏览器---------------
from appium import webdriver
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'6',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息:
    #adb shell dumpsys activity recents | findstr intent={
    'browserName':'Chrome',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    # #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    # 'automationName':'UiAutomator2',#或者UiAutomator1
    # 'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
    'chromedriverExecutableDir':r'F:\webdriver\chromedriver_v81'#驱动路径
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
driver.find_element_by_css_selector('div.con-wrap>input').click()
driver.find_element_by_css_selector('div.con-wrap>input').send_keys('pyhton\n')
input('nnn')
driver.quit()