#coding=utf8
# auther:shixingjian  time:2020/07/09
from lib.ApiLogin import LoginClass
from lib.ApiLesson import LessonClass
from lib.GetExcelData import get_excelData
import json
import pytest
import time
import allure
@allure.feature('课程模块')#一级标题
@pytest.mark.Lesson(order = 2)
class TestLesson:#测试用例类
    def setup_class(self):
        self.session = LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}')
        return self.session
    @allure.story('新增课程')
    @allure.title('新增课程用例')
    @pytest.mark.lesson_add
    @pytest.mark.parametrize('inData,expreValue',get_excelData('2-课程模块',2,25,6,8))
    def test_add_lesson(self,inData,expreValue):
        strRandom = str(int(time.time()*10000))
        inData = inData.replace('{{courseName}}',strRandom)
        res = LessonClass().add_lesson(self.session,inData)
        assert res['retcode'] == json.loads(expreValue)['code']

    @allure.story('列出课程')
    @allure.title('列出课程用例')
    @pytest.mark.lesson_list #标签，选择执行pytest test_lesson.py -s -m=add
    @pytest.mark.parametrize('inData,expreValue',get_excelData('2-课程模块',26,38,6,8))
    def test_list_lesson(self,inData,expreValue):
        res = LessonClass().list_lesson(self.session,json.loads(inData))
        assert res['retcode'] == json.loads(expreValue)['code']


    # @pytest.mark.parametrize('inData,expreValue',get_excelData('2-课程模块',26,38,6,8))
    # def test_modify_lesson(self,inData,expreValue):
    #     inData = {"name":"math","desc":"2","display_idx":"3"}
    #     res = LessonClass().modify_lesson(self.session,274,json.loads(inData))
    #     assert res["retcode"] == json.loads(expreValue)['code']

    @allure.story('删除课程')
    @allure.title('删除课程用例')
    @pytest.mark.lesson_delete
    @pytest.mark.parametrize('inData,expreValue',get_excelData('2-课程模块',39,46,6,8))
    def test_delete_lesson(self,inData,expreValue):
        res = LessonClass().delete_lesson(self.session,json.loads(inData))
        assert res['retcode'] == json.loads(expreValue)['code']


if __name__ == '__main__':
    session = TestLesson().setup_class()
    TestLesson().test_list_lesson()#不能直接运行，没有运行setup_class

