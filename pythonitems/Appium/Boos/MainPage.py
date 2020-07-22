#coding=utf8
# auther:shixingjian  time:2020/07/16
from Boos.BasePage import BasePage
class MainPage(BasePage):
    def __init__(self):
        super().__init__()#执行父类构造方法
        #元素定位方法
        self.search_button = ('xpath','//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]/*')#搜索按钮定位
        self.search_input = ('id','com.hpbr.bosszhipin:id/et_search')#搜索框
        self.search_res = ('id','com.hpbr.bosszhipin:id/tv_filtered_name')#搜索结果列表
        self.jobs_list = ('id','com.hpbr.bosszhipin:id/view_job_card')#工作元素列表
        self.job_name = ('id','com.hpbr.bosszhipin:id/tv_position_name')#岗位名称
        self.job_salary = ('id','com.hpbr.bosszhipin:id/tv_salary_statue')#薪资
        self.job_company = ('id','com.hpbr.bosszhipin:id/tv_company_name')#公司
        self.my_button = ('id','com.hpbr.bosszhipin:id/cl_tab_4')#我的按钮
    def search_button_element(self):#获取搜索按钮
        return self.get_Element(self.search_button)
    def search_input_element(self):
        return self.get_Element(self.search_input)
    def search_res_element(self):
        return self.get_Element(self.search_res)
    def jobs_list_elements(self):
        return self.get_Elements(self.jobs_list)
    def job_name_element(self):
        return self.get_Element(self.job_name)
    def job_salary_element(self):
        return self.get_Element(self.job_salary)
    def job_company_element(self):
        return self.get_Element(self.job_company)
    def my_button_element(self):
        return self.get_Element(self.my_button)

if __name__ == '__main__':
    MainPage().search_button_elements()[1].click()