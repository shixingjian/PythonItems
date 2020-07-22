#coding=utf8
# auther:shixingjian  time:2020/07/16
#准备自动化配置信息
class Caps:
    @classmethod
    def get_Caps(self,plathform_version=6,
        package_name='com.hpbr.bosszhipin',
        activity_name='.module.launcher.WelcomeActivity'):
        caps = {
        #移动设备平台
        'platformName':'Android',
        #平台OS版本号,写整数位即可
        'plathformVersion':str(plathform_version),
        #设备的名称--值可以随便写
        'deviceName':'test0106',
        #提供被测app的信息-包名，入口信息:
        #adb shell dumpsys activity recents | findstr intent={
        'appPackage':package_name,
        'appActivity':activity_name,
        #确保自动化之后不重置app
        'noReset':True,
        #设置session的超时时间，单位秒
        'newCommandTimeout':6000,
        #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
        'automationName':'UiAutomator2',#或者UiAutomator1
        'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
        }
        return caps

HOST = 'http://127.0.0.1:4723/wd/hub'
if __name__ == '__main__':
    print(Caps.get_Caps())