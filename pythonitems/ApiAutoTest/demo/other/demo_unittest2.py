#coding=utf8
# auther:shixingjian  time:2020/07/04
import unittest
from ddt import ddt,data
from lib.excelManage import readExcel
from lib.sendCorseRequest import sendCourseRequest
import time
import json
# path = r'../../data/教管系统接口测试用例-v1.4.xls'
# list = readExcel(path,2)

# @ddt
class UnittestDemo2(unittest.TestCase):
    #环境初始化方法，类级别的
    @classmethod
    def setUpClass(cls):
        print('setUp方法运行了\r\n')
    #测试加法
    def test_001(self):
        print(">>>用例1运行了")

    #测试减法
    # @unittest.skip("不想测试的原因")
    def test_002(self):
        # assert 1==1
            self.assertEqual(1,2,'123')
            print(">>>用例2运行了")

    #测试乘法
    def test_003(self):
        print(">>>用例3运行了")

    # 测试加法
    def test_004(self):
        print(">>>用例4运行了")

    def test_005(self):

        print(">>>用例5运行了")

