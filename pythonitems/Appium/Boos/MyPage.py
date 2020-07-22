#coding=utf8
# auther:shixingjian  time:2020/07/18
from Boos.BasePage import BasePage
class MyPage(BasePage):
    def __init__(self):
        super().__init__()
        self.btn_setting = ('id','com.hpbr.bosszhipin:id/iv_general_settings')#设置按钮
        self.btn_user = ('xpath','//*[@text="账号与绑定"]')#账户与绑定按钮
        self.btn_modifytel = ('xpath','//*[@text="修改手机号"]')#修改手机号按钮
        self.btn_modifypwd = ('xpath','//*[@text="修改密码"]')#修改密码按钮
        self.et_oldpwd = ('id','com.hpbr.bosszhipin:id/et_old')#旧密码输入框
        self.et_newpwd = ('id','com.hpbr.bosszhipin:id/et_new')#新密码输入框
        self.et_confirmpwd = ('id','com.hpbr.bosszhipin:id/et_new_confirm')#确认密码输入框
        self.btn_save = ('id','com.hpbr.bosszhipin:id/btn_save')#确认修改按钮
        self.btn_logout = ('id','com.hpbr.bosszhipin:id/btn_logout')#退出登录按钮
        self.tv_positive = ('id','com.hpbr.bosszhipin:id/tv_positive')#确定退出登录按钮

    def getele_btn_setting(self):
        return self.get_Element(self.btn_setting)
    def getele_btn_user(self):
        return self.get_Element(self.btn_user)
    def getele_btn_modifytel(self):
        return self.get_Element(self.btn_modifytel)
    def getele_btn_modifypwd(self):
        return self.get_Element(self.btn_modifypwd)
    def getele_et_oldpwd(self):
        return self.get_Element(self.et_oldpwd)
    def getele_et_newpwd(self):
        return self.get_Element(self.et_newpwd)
    def getele_et_confirmpwd(self):
        return self.get_Element(self.et_confirmpwd)
    def getele_btn_save(self):
        return self.get_Element(self.btn_save)
    def getele_btn_logout(self):
        return self.get_Element(self.btn_logout)
    def getele_tv_positive(self):
        return self.get_Element(self.tv_positive)
if __name__ == '__main__':
    from Boos.MainPage import MainPage
    MainPage().my_button_element().click()
    MyPage().getele_btn_setting().click()