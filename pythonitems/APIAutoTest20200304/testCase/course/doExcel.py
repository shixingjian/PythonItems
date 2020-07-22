from lib.excelManager import readExcel,getNewExcel
from lib.sendCourseReq import sendCourseReq
import json

#1.定义文件路径变量
filePath=r'E:\ProjectCodeForPy\APIAutoTest20200304\data\教管系统-测试用例V1.2.xls'
savePath=r'E:\ProjectCodeForPy\APIAutoTest20200304\report\测试结果.xls'
#2.从excel中读取测试用例
retDataList=readExcel(filePath,0)
#3.复制一个新的工作簿
workBookNew=getNewExcel(filePath)
workSheetNew=workBookNew.get_sheet(0)

# print(retDataList)
for i in range(0,len(retDataList)):
    #4.调用函数，并执行
    retDict=sendCourseReq(retDataList[i])
    colus6 = json.loads(retDataList[i][6])  # 断言结果
    #5.断言结果写入excel
    if (retDict['retcode'] == colus6['code']):
        workSheetNew.write(i+1,7,'pass')
    else:
        workSheetNew.write(i + 1, 7, 'fail')
        #某些测试用例，可能测试不通过不返回错误原因。
        if 'reason' in retDict.keys():
            workSheetNew.write(i + 1, 8, retDict['reason'])
#6.保存excel
workBookNew.save(savePath)

