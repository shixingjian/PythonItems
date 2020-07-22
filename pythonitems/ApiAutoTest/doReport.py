#coding=utf8
# auther:shixingjian  time:2020/07/02
import unittest
from ClassicHTMLTestRunner import HTMLTestRunner

#1.构建测试套件test_suite
#1-1.方法一：用例逐个添加到suite
# suit = unittest.TestSuite()
# suit.addTest(UnittestDemo('test_001'))
# suit.addTest(UnittestDemo('test_002'))
# suit.addTest(UnittestDemo('test_004'))
# suit.addTest(UnittestDemo('test_003'))

#1-2.方法二：用例放入列表中，再添加到suite
# suit = unittest.TestSuite()
# list = [UnittestDemo('test_001'),UnittestDemo('test_002'),UnittestDemo('test_003'),UnittestDemo('test_004')]
# suit.addTests(list)

#1-3.方法三：通过TestLoader类的discover方法来
suit = unittest.defaultTestLoader.discover('demo.other',pattern="demo_unittest3.py")

#2.运行用例，查看结果
#2-1.第一种情况，使用unittest自带的报告导出
# runner = unittest.TextTestRunner()
# runner.run(suit)

#2-2.第二种情况，使用HtmlTestRunner
reportFile = open('./report/接口测试html测试报告.html','wb')
runner = HTMLTestRunner(tester='shixingjian',title='HtmlTestRunner测试报告',description='接口自动化测试',
                        stream=reportFile,verbosity=2)
runner.run(suit)
#2-1.第一种情况，使用unittest自带的报告导出
