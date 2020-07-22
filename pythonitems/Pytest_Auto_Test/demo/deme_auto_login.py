#coding=utf8
# auther:shixingjian  time:2020/07/08
import xlrd
import json
from demo.demo_login import login
from xlutils.copy import copy
url_Excel = '../data/教管系统接口测试用例-v1.4.xls'
url_sava = '../report/教管系统接口测试用例-1.4.xls'
workBook = xlrd.open_workbook(url_Excel,formatting_info=True)#原格式打开
workSheet = workBook.sheet_by_name("1_登录接口")

new_wordBook = copy(workBook)#复制新workbook
new_sheet = new_wordBook.get_sheet(1)
def login_api_test(row):
     #1.---------------从Excel读数据---------------------
     #库：openpyxl、xlrd、xlwd、xlutils
    # formatting_info=True 不支持xlsx
    # name_sheet = workBook.sheet_names()
    # rowdata = workSheet.row_values(1)#第一行数据
    # coldata = workSheet.col_values(0)#第一列数据
    # print(rowdata,coldata)
    login_data = workSheet.cell_value(row,6)#单元格数据
    username = json.loads(login_data)['username']
    password = json.loads(login_data)['password']
    retinfo = login(username,password)
     #2.--------------------Excel写数据----------------------
    #获取实际结果
    real_res = retinfo['retcode']
    # print(real_res)
    #获取预期结果
    expre_res = json.loads(workSheet.cell_value(row,8))['retcode']
    #获取用例编号
    test_no = workSheet.cell_value(row,1)
    reason = ''
    if 'reason' in retinfo.keys():
        reason = retinfo['reason']
        if real_res == expre_res:
            test_res = 'pass'
            print(f'----{test_no}-----pass-------{reason}----')
        else:
            test_res = 'fail'
            print(f'----{test_no}-----fail-------{reason}----')
    else:
        test_res = 'pass'
        print(f'----{test_no}-----pass-------{reason}----')
    new_sheet.write(row,9,test_res)
    #保存
    new_wordBook.save(url_sava)
if __name__ == '__main__':
    # login_api_test(2)
    i = 1
    for i in range(1,5):
        login_api_test(i)