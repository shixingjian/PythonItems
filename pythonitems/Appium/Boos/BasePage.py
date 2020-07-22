#coding=utf8
# auther:shixingjian  time:2020/07/16
from appium import webdriver
from Boos.config import HOST,Caps
from time import sleep
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class Driver:
    _driver1 = None
    @classmethod
    def get_driver(cls):
        if cls._driver1 == None:
            try:
                cls._driver1 = webdriver.Remote(HOST,Caps.get_Caps())#远程连接手机
            except:
                raise NameError("Driver不存在")
        # else:
        #     raise NameError("driver不存在")
        return cls._driver1


class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()
        # self.driver.implicitly_wait(10)  # 隐式等待
    #获取页面元素的方法
    def get_Element(self,locator):
        WebDriverWait(self.driver, 10, 0.5).until(ec.visibility_of_element_located((locator)),message='获取元素超时')
        return self.driver.find_element(*locator)#返回元素对象

    def get_Elements(self,locator):
        WebDriverWait(self.driver, 10, 0.5).until(ec.visibility_of_all_elements_located((locator)),message='获取元素超时')
        return self.driver.find_elements(*locator)#返回元素对象列表
    def del_driver(self):
        self.driver.quit()
    # def __del__(self):
    #     self.driver.quit()

    def swipe_up(self,n):#上划
        '''
        :param n: 滑动次数
        :return:
        '''

        win_size = self.driver.get_window_size()
        start_x = win_size['width']/2
        start_y = win_size['height']/4*3
        end_x = start_x
        end_y = win_size['height']/4
        i = 0
        sleep(1)
        if i in range(n):
            self.driver.swipe(start_x,start_y,end_x,end_y)
            i += 1
            sleep(1)

if __name__ == '__main__':
    # eles = BasePage().get_Element(('xpath','//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/*')).click()#点击搜索键
    # BasePage().get_Element(('id','com.hpbr.bosszhipin:id/et_search')).send_keys('软件测试')
    # input('nnn')
    # BasePage().deldriver()
    BasePage().swipe_up(6)

