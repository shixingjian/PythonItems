#coding=utf8
# auther:shixingjian  time:2020/07/04
from lib.excelManage import readExcel,getNewExcel
from lib.sendCorseRequest import sendCourseRequest
from lib.courseLib import login
import time
import json
sessionid = login("auto","sdfsdfsdf")
#1-1定义path
path = r'../../data/教管系统接口测试用例-v1.4.xls'
savePath = r'../../report/教管系统接口测试结果-v2.1.xls'
#1-2读取Excel测试用例
lists = readExcel(path,2)
#3.将执行结果写入Excel
#3.1-复制一个新的excel
workBookNew = getNewExcel(path)
#3.2-在新的excel得到第一个工作表
workBookSheet = workBookNew.get_sheet(2)
#4.执行测试用例
for i in range(0,len(lists)):
    row = lists[i]
    # sessionid = login("auto", "sdfsdfsdf")
    dictBody = sendCourseRequest(row,sessionid)
    # dictBodys.append(dictBody)
    time.sleep(0.01)
    # 在第7,8列写结果
    resValue = json.loads(row[8])
    if dictBody['retcode'] == resValue['code']:
        print(row[0],"测试通过")
        workBookSheet.write(i+1,9,'pass')
    else:
        print(row[0], "测试不通过")
        workBookSheet.write(i+1,9,'fail')
        if 'reason' in dictBody.keys():
            workBookSheet.write(i+1,10,dictBody['reason'])
        # print(dictBody['reason'])
#5.保存到report
workBookNew.save(savePath)
