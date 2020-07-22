import unittest
import json
from ddt import ddt,data

#上节课封装的一些函数
from lib.excelManager import readExcel,getNewExcel
from lib.sendCourseReq import sendCourseReq


#下面这2行代码，是从excel中读取测试用例。
filePath=r'C:\Users\yjj\PycharmProjects\untitled5\APIAutoTest20200304\data\教管系统-测试用例V1.2.xls'
mydata=readExcel(filePath,0) #上节课封装的函数

# mydata=[[1,2,3],[3,4,7],[1,3,5]]

#输出回车
print('\r\n')

@ddt
class DdtDemo(unittest.TestCase):

    @data(*mydata)
    def test09(self,aaa1):
        retDict = sendCourseReq(aaa1)
        colus6 = json.loads(aaa1[6])  # 断言结果
        # 5.测试失败原因
        v_reason=''
        #上节课的知识，测试失败可能没有返回reason
        if 'reason' in retDict.keys():
            v_reason=retDict['reason']
        #接口返回结果和excel中的进行比较
        self.assertEqual(retDict['retcode'],colus6['code'],v_reason)
        print('>>>>>>测试通过！！！')
        print("<<<<<<<测试ok")

