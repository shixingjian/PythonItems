#-*-coding:utf-8-*-
#@Time:2020/4/910:02
#@Author:freya
#@File:dem0_unnittest03.py
from demo.other.demo_calculator import Calculator
import unittest
from ddt import ddt,data
from lib.excelManage import readExcel
import time
from lib.sendCourseRequest import SendCourceRequest
import json
"""
    UnitTest结合DDT语法学习
"""
mydata=[[1,2,3],[3,4,7],[4,5,9]]

path=r'../../data/教管系统-测试用例V1.2.xls'
#2-读取测试用例
mydata2=readExcel(path,1)
@ddt
class UnittestDemo3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calculator=Calculator(12,3)
        print('setUp方法运行了\r\n')

    #1. 测试加法
    def test_001(self):
        print('>>>>用例1运行了')
        result=self.calculator.add()
        self.assertEqual(result,15)

    #2. 测试减法
    def test_002(self):
        print('>>>>用例2运行了')
        result=self.calculator.sub()
        self.assertEqual(result,9)

    #3. 测试乘法
    def test_003(self):
        print('>>>>用例3运行了')
        result=self.calculator.mul()
        self.assertEqual(result,36)

    #4. 测试除法
    def test_004(self):
        print('>>>>用例4运行了')
        result=self.calculator.div()
        self.assertEqual(result,4)

    # 5. 测试加法2
    @data(*mydata)
    def test_005(self,data):
        result=self.calculator.add2(data[0],data[1])
        self.assertEqual(result,data[2])
        print('>>>>用例5运行了')

    # 6. 批量执行excel测试用例
    @data(*mydata2)
    def test_006(self,row):
        # print(row)
        dictBody = SendCourceRequest(row)
        time.sleep(0.001)
        test = json.loads(row[6])
        print('>>>>用例6运行了')
        # if 'reason' in dictBody.keys():
        #     self.assertEqual(dictBody['retcode'], test['code'],dictBody['reason'])
        # else:
        self.assertEqual(dictBody['retcode'], test['code'])




