#coding=utf8
# auther:shixingjian  time:2020/07/09
import pytest
from lib.ApiLogin import LoginClass
from lib.ApiLesson import LessonClass
import json
@pytest.fixture(scope="module",autouse='ture')#scope作用域autouse是否自动执行------环境初始化，数据去清除
def delete_all_lesson(request):
    # 登录
    session = LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}')
    # 列出所有课程
    lessonlist = LessonClass().list_lesson(session,{"action":"list_course","pagenum":"1","pagesize":"999"})['retlist']
    #删除所有课程
    # while lessonlist != []:
    for one in lessonlist:
        LessonClass().delete_lesson(session,{'action':'delete_course','id':one['id']})
    print('------------cleandown-------------')

    #新增课程数据
    # for i in range(1,7):
    #     lessonData = {"name":f"english{i:0>3}","desc":"1","display_idx":f"{i}"}
    #     LessonClass().add_lesson(session,json.dumps(lessonData))
    #环境数据清除，teardown
    def fin():
        # 列出所有课程
        lessonlist = LessonClass().list_lesson(session, {"action": "list_course", "pagenum": "1", "pagesize": "999"})[
            'retlist']
        # 删除所有课程
        # while lessonlist != []:
        for one in lessonlist:
            LessonClass().delete_lesson(session, {'action': 'delete_course', 'id': one['id']})
        print('------------cleandown-------------')


        # 新增课程数据
        for i in range(1,7):
            lessonData = {"name":f"english{i:0>3}","desc":f"描述{i}","display_idx":f"{i}"}
            LessonClass().add_lesson(session,json.dumps(lessonData))
        print("-----环境恢复-------")
    request.addfinalizer(fin)