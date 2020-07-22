#coding=utf8
# auther:shixingjian  time:2020/07/16
from Boos.MainPage import MainPage
from Boos.BasePage import BasePage
class MainPageAction(MainPage):
    # def __init__(self):
    #     super().__init__()
    def list_jobs(self):
        self.search_button_element().click()#点击搜索框按钮
        self.search_input_element().click()#点击搜索框按钮
        self.search_input_element().send_keys("软件测试")#搜索框输入软件测试
        self.search_res_element().click()#点击一个符合条件的搜索结果
        self.jobs = self.jobs_list_elements()
        for job in self.jobs:
            name = job.find_element(*self.job_name)
            salray = job.find_element(*self.job_salary)
            companys = job.find_elements(*self.job_company)
            if companys:
                print('%s|%s|%s' % (name.text, salray.text, companys[0].text))
if __name__ == '__main__':
    MainPageAction().list_jobs()
    input('kkk')
    BasePage().del_driver()
