#coding=utf8
# auther:shixingjian  time:2020/07/04
import unittest
from ddt import ddt,data
from lib.excelManage import readExcel
from lib.sendCorseRequest import sendCourseRequest
from lib.courseLib import delete_course,list_course
import time
import json
from lib.courseLib import login
from lib.mysqlManage import delete_All_Course
filePath = r'F:/pythonitems/ApiAutoTest/data/教管系统接口测试用例-v1.4.xls'
list = readExcel(filePath,2)
print(len(list))

@ddt
class UnittestDemo3(unittest.TestCase):
    # 环境初始化方法，类级别的
    @classmethod
    def setUpClass(cls):
        cls.sessionid = login("auto", "sdfsdfsdf")
        # cls.clearData()
        delete_All_Course()
        print('setUp方法运行了\r\n')

    @classmethod
    def tearDownClass(cls):
        # cls.clearData()
        delete_All_Course()
        print('setUp方法运行了\r\n')
    @classmethod
    def clearData(self):
        listData = list_course(1,999,self.sessionid)
        i = 0
        for item in listData['retlist']:
            delete_course(item['id'],self.sessionid)
            i = i+1
        print("本次删除的条数：",i)
    # 测试用例2
    # @unittest.skip("用例2不执行的原因")
    def test_002(self):
        # assert 1==1
        self.assertEqual(1,1)
        print(">>>用例2运行了")
    # 测试用例3
    def test_003(self):
        print(">>>用例3运行了")
    # 测试用例4
    def test_004(self):
        print(">>>用例4运行了")
    @data(*list)#*表示去掉外层中括号
    def test_005(self,row):
        dictBoby = sendCourseRequest(row,self.sessionid)
        time.sleep(0.01)
        test = json.loads(row[8])#字符串----》字典
        print(dictBoby)
        retreason = ''
        if 'reason' in dictBoby.keys():
            retreason = dictBoby['reason']
        print(retreason)
        self.assertEqual(test['code'],dictBoby['retcode'],retreason)
        print(">>>用例5运行了")
