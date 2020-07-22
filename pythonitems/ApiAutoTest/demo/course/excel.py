#coding=utf8
# auther:shixingjian  time:2020/07/03
import xlrd
#1.读取Excel中的数据
def readExcel(filePath,sheet_index):
    #2.打开Excel，读取workbook对象
    wordBook = xlrd.open_workbook(filePath)
    #3.从工作簿中读取worksheet对象
    workSheet = wordBook.sheet_by_index(sheet_index)
    nrow = workSheet.nrows
    listData = []
    for i in range(1,nrow):
        list = workSheet.row_values(i)
        listData.append(list)
    return listData
if __name__ == '__main__':
    filepath = r'../../data/教管系统接口测试用例-v1.4.xls'
    print(readExcel(filepath,2))
