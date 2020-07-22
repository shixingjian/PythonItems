import unittest
from demo.other.demo_unittest01 import UnittestDemo1
from demo.other.demo_unittest02 import UnittestDemo2
from ClassicHTMLTestRunner import HTMLTestRunner
#（一）构建测试套件 test_suite
#1-1 方法一：用例逐个添加到suite
# suite=unittest.TestSuite()
# suite.addTest(UnittestDemo1("test01"))
# suite.addTest(UnittestDemo1("test02"))
# suite.addTest(UnittestDemo1("test03"))
# suite.addTest(UnittestDemo1("test04"))
#
# suite.addTest(UnittestDemo2("test01"))
# suite.addTest(UnittestDemo2("test02"))
# suite.addTest(UnittestDemo2("test04"))

#1-2 方法二：用例放入列表中，再添加到suite
# list=[UnittestDemo1("test01"),UnittestDemo1("test02"),UnittestDemo1("test03"),UnittestDemo1("test04"),
# UnittestDemo2("test01"),UnittestDemo2("test02")]
# suite.addTests(list)


#1-3 方法三：通过TestLoader类的discover 方法来
suite=unittest.defaultTestLoader.discover('demo.other',pattern="demo_unittest02.py")


#（二）测试运行器查看结果
#2-1 第1种情况：不使用HtmlTestRunner插件
# runner=unittest.TextTestRunner()
# runner.run(suite)

#2-2 第2种情况：使用【经典版】HtmlTestRunner插件
reportFile=open(r'C:\Users\yjj\PycharmProjects\untitled5\APIAutoTest20200304\report\htmlReport.html ','wb')
runner001=HTMLTestRunner(stream=reportFile,verbosity=2,description='用例执行详细信息',title='测试报告',tester='杨静')
runner001.run(suite)

