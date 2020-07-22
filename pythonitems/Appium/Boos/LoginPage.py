#coding=utf8
# auther:shixingjian  time:2020/07/18
from Boos.BasePage import BasePage
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.tv_pwdlogin = ('id','com.hpbr.bosszhipin:id/tv_password_login')#账号登录按钮
        self.et_password = ('id','com.hpbr.bosszhipin:id/et_password')#密码输入框
        self.btn_login = ('id','com.hpbr.bosszhipin:id/btn_login')#登录按钮
    def getele_tv_pwdlogin(self):
        return self.get_Element(self.tv_pwdlogin)
    def getele_et_password(self):
        return self.get_Element(self.et_password)
    def getele_btn_login(self):
        return self.get_Element(self.btn_login)
if __name__ == '__main__':
    LoginPage().getele_tv_pwdlogin().click()