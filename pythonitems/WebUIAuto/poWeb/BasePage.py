#coding=utf8
# auther:shixingjian  time:2020/07/15
from selenium import webdriver
from setting import DIMIN,TIMEOUT,POLL_FREQUENCY
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
class Driver:
    _driver = None#私有对象,只能在类里使用
    @classmethod
    def get_driver(cls,broswer = 'Chrome'):#类方法，类名点方法直接调用
        '''
        :param broswer: 浏览器
        :return: 浏览器对象
        '''
        if cls._driver == None:#创建多页时不为空
           if broswer == "Chrome":
                cls._driver = webdriver.Chrome()
           elif broswer == "Firefox":
               cls._driver = webdriver.Firefox()
           else:
               raise NameError("浏览器对象不存在")
        return cls._driver

class BasePage:
    def __init__(self):
        #封装浏览器对象
        self.driver = Driver.get_driver()#静态字段，可以通过类名访问
        self.get_url()#调用访问网址方法
    def get_url(self):#访问网址方法
        self.driver.get(DIMIN)
    def get_Element(self,locator):
        '''
        显示等待
        :param locator: 元素对象定位方法
        :return: 元素对象
        '''
        WebDriverWait(driver=self.driver,timeout=TIMEOUT,poll_frequency=POLL_FREQUENCY).until(
            ec.visibility_of_element_located(locator)#显示等待
        )
        return self.driver.find_element(*locator)#返回元素对象
    def get_Elements(self,locator):
        WebDriverWait(self.driver,TIMEOUT,POLL_FREQUENCY).until(
            ec.visibility_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

if __name__ == '__main__':
    from selenium.webdriver.common.by import By
    import time
    BasePage().get_Element((By.CSS_SELECTOR,"button[class='btn btn-success']")).click()
    time.sleep(2)
    print(BasePage().get_Elements((By.CSS_SELECTOR,'tbody>tr')))