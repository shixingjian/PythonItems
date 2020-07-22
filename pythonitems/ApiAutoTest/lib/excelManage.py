#coding=utf8
# auther:shixingjian  time:2020/07/03
import xlrd
from xlutils.copy import copy
#1.读取Excel中的数据
def readExcel(filePath,sheet_index):
    #2.打开Excel，读取workbook对象
    wordBook = xlrd.open_workbook(filePath)
    #3.从工作簿中读取worksheet对象
    workSheet = wordBook.sheet_by_index(sheet_index)
    # workSheet = wordBook.sheet_by_name("课程管理")
    #4.从worksheet中逐步读取数据放入列表中
    nrows = workSheet.nrows#有多少行数据
    listData = []
    for i in range(1,nrows):
        row = workSheet.row_values(i)#读取每行的值并返回列表
        listData.append(row)
    # 5.返回数据列表
    return listData

def getNewExcel(filePath):
    # 1-1.打开Excel，得到workbook对象
    workBook = xlrd.open_workbook(filePath,formatting_info=True)#formatting_info=True带格式复制
    # 1-2.复制一个新的工作簿
    newWorkNew = copy(workBook)
    return newWorkNew

if __name__ == '__main__':
    filepath = r'F:/pythonitems/ApiAutoTest/data/教管系统接口测试用例-v1.4.xls'
    readExcel(filepath,2)

