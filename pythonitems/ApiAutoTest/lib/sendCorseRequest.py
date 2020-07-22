#coding=utf8
# auther:shixingjian  time:2020/07/03
from lib import excelManage
import json
import time
from lib.courseLib import add_course,delete_course,list_course
#将Excel表中使用excelManage获取的数据使用courseLib中的函数发送出去并返回结果
#传入一行Excel数据行（）列表格式，返回请求结果（字典格式）
#1.定义函数
def sendCourseRequest(row,sesionID):
    data = json.loads(row[6])  # 字符串--->字典
    if 'add' in row[0]:
        randomStr = str(int(time.time()*10000))
        course_name =data['name'].replace('{{courseName}}',randomStr)
        dictBody = add_course(course_name,data["desc"],data['display_idx'],sesionID)
        # resValue = json.loads(row[8])
        # if dictBody['retcode'] == resValue['code']:
        #     print(row[0],"测试通过")
        # else:
        #     print(row[0], "测试不通过")
    elif 'list' in row[0]:
        pagenum = data['pagenum']
        pagesize = data['pagesize']
        dictBody = list_course(pagenum,pagesize,sesionID)
    elif 'delete'in row[0]:
        dictBody = delete_course(data['id'],sesionID)
    # elif 'modify'in row[0]:
    #     pass
    return dictBody
if __name__ == '__main__':
    filepath = r'../data/教管系统接口测试用例-v1.4.xls'
    listData = excelManage.readExcel(filepath,2)
    for rowlist in listData:
        sendCourseRequest(rowlist)
    time.sleep(0.01)

