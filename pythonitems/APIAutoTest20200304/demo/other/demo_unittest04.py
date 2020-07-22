#-*-coding:utf-8-*-
#@Time:2020/4/910:17
#@Author:freya
#@File:demo_unittest04.py
from demo.other.demo_calculator import Calculator
import unittest
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
    def test_005(self):
        print('>>>>用例5运行了')
        result=self.calculator.add2(5,5)
        self.assertEqual(result,10)
