#coding=utf8
# auther:shixingjian  time:2020/07/04
import unittest
from lib.courseLib import list_course,delete_course,add_course
import time
from lib.courseLib import login
class UnittestDemo(unittest.TestCase):
    #环境初始化方法，类级别的
    @classmethod
    def setUpClass(cls):
        cls.sesionid = login("auto", "sdfsdfsdf")#静态变量/类变量
        cls.clearData()
    #数据清除方法，类级别的
    @classmethod
    def tearDownClass(cls):
        cls.clearData()
    @classmethod
    def clearData(self):#类方法
        # 数据清除：
        listData = list_course(1, 999,self.sesionid)
        i = 0
        for item in listData['retlist']:
            delete_course(item['id'],self.sesionid)
            i += 1
        print('本次删除了数据的条数', i,'\n')
    #测试加法
    def test_001(self):#实例方法可以使用类变量
        #新增课程
        courseName = "初中化学" + str(int(time.time() * 10000))
        dictBody1 = add_course(courseName,'初中化学',0,self.sesionid)
        # 列出课程
        dictBody2 = list_course(1,500,self.sesionid)
        retlists = dictBody2['retlist']
        #从表中查询该课程是否存在
        exit = 0
        for item in retlists:
            if item['id'] == dictBody1['id']:
                exit = 10
                break
        self.assertEqual(exit,10)

        print(">>>用例1运行了")

    #测试减法
    # @unittest.skip("不想测试的原因")
    def test_002(self):
        # assert 1==1
        self.assertEqual(1,1,'....原因测试不通过')
        print(">>>用例2运行了")

    #测试乘法
    def test_003(self):
        print(">>>用例3运行了")

    # 测试加法
    def test_004(self):
        print(">>>用例4运行了")

