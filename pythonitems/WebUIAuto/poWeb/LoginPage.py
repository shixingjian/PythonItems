#coding=utf8
# auther:shixingjian  time:2020/07/15
from poWeb.BasePage import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()#执行父类的构造方法
        self.username_locator = (By.ID,'username')#元素定位方法
        self.password_locator = (By.ID,'password')
        self.loginbutton_locator = (By.TAG_NAME,'button')
    #抽离具体的元素控件
    def username_element(self):
        return self.get_Element(self.username_locator)
    #密码输入框元素
    def password_element(self):
        return self.get_Element(self.password_locator)
    #登录按钮
    def loginbutton_element(self):
        return self.get_Element(self.loginbutton_locator)

class LoginPageAction(LoginPage):#执行登录动作
    def login(self):
        self.username_element().clear()
        self.password_element().clear()
        self.username_element().send_keys('auto')
        self.password_element().send_keys('sdfsdfsdf')
        self.loginbutton_element().click()
if __name__ == '__main__':
    LoginPageAction().login()