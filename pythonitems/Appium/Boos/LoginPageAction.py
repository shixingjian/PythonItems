#coding=utf8
# auther:shixingjian  time:2020/07/18
from Boos.LoginPage import LoginPage
from Boos.BasePage import BasePage
class LoginPageAction(LoginPage):
    def Login(self):
        self.getele_tv_pwdlogin().click()#点击账号登录
        password = input('请输入密码：')
        self.getele_et_password().send_keys(password)#输入密码
        self.getele_btn_login().click()#点击登录


if __name__ == '__main__':
    LoginPageAction().Login()
    input('...')
    BasePage().del_driver()