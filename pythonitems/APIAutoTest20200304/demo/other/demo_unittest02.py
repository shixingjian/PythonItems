import unittest


class UnittestDemo2(unittest.TestCase):

    #测试套件：第二对方式-【方法级别】
    def setUp(slef):
        print('>>>>方法级别的setUp方法运行了\r\n')

    def tearDown(self):
        print('>>>>方法级别的tearDown方法运行了\r\n')


    # 测试用例1
    def test01(self):
        print('>>>>测试用例1运行了')

    # 测试用例2
    def test02(self):
        list=readExcel()
        for i in range():
            pass
            self.assertEqual(1,3,'xx原因测试不通过')
            print('>>>>测试用例2运行了')

    # 测试用例3
    def test03(self):
        print('>>>>测试用例3运行了')

    # 测试用例4
    def test04(self):
        print('>>>>测试用例4运行了')
