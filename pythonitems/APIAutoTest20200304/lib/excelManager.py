import xlrd
from  xlutils.copy  import copy
# 读取excel 中的数据
# 功能：传递excel的路径+名称、第几个工作表
def readExcel(filePath,sheet_index):
    # 1-1 打开Excel，获取【workBook】 对象
    workBook=xlrd.open_workbook(filePath)

    # 1-2 从工作簿中，获取【workSheet】对象
    workSheet=workBook.sheet_by_index(sheet_index)

    # 1-3 对【workSheet】工作表进行循环-逐行取出数据--放入列表中
    retDataList=[]
    rows=workSheet.nrows
    for i in range(1,rows):
        oneRow=workSheet.row_values(i)
        retDataList.append(oneRow)

    # 1-4 返回数据列表
    return retDataList

# a=readExcel(r'E:\ProjectCodeForPy\APIAutoTest20200304\data\教管系统-测试用例V1.2.xls',0)
# print(a)

#2.从一个工作簿中复制一个新的工作簿
def getNewExcel(filePath):
    # 1-1 打开Excel，获取【workBook】 对象
    workBook = xlrd.open_workbook(filePath,formatting_info=True)

    # 1-2 复制一个全新的工作簿并返回
    workBookNew=copy(workBook)

    return workBookNew

