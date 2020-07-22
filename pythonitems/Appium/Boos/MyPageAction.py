#coding=utf8
# auther:shixingjian  time:2020/07/18
from Boos.MyPage import MyPage
from Boos.MainPage import MainPage
from Boos.BasePage import BasePage
from Boos.LoginPageAction import LoginPageAction
from time import sleep
class MyPageAction(MyPage):
    # def __init__(self):
    #     MainPage().my_button_element().click()  # 点击我的
    #修改密码
    def modify_password(self):
        MainPage().my_button_element().click()  # 点击我的
        self.getele_btn_setting().click()#点击设置
        self.getele_btn_user().click()#点击用户账户
        self.getele_btn_modifypwd().click()#点击修改密码
        self.getele_et_oldpwd().send_keys('123')#输入旧密码
        self.getele_et_newpwd().send_keys('123')#输入新密码
        self.getele_et_confirmpwd().send_keys('123')#确认密码输入框
        self.getele_btn_save().click()#确认密码按钮
    def login_exit(self):
        MainPage().my_button_element().click()  # 点击我的
        self.getele_btn_setting().click()  # 点击设置
        MyPage().swipe_up(1)
        self.getele_btn_logout().click()  # 点击退出登录
        self.getele_tv_positive().click() # 确定点击退出登录


if __name__ == '__main__':
    # MyPageAction().modify_password()
    MyPageAction().login_exit()
    sleep(3)
    LoginPageAction().Login()
    input('nnn')
    BasePage().del_driver()