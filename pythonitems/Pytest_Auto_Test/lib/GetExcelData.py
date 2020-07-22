#coding=utf8
# auther:shixingjian  time:2020/07/10
import xlrd
#获取Excel数据
def get_excelData(sheetName,startRow,endRow,reqCol,expreCol):
    '''
    :param sheetName: 表名
    :param startRow:开始行号（Excel行号）
    :param endRow:结束行号（Excel行号）
    :param reqCol:请求参数列数
    :param expreCol:预期结果列数
    :return:[(请求参数字符串,预期结果字符串),(请求参数字符串,预期结果字符串)...]
    '''
    excel_url = '../data/教管系统接口测试用例-v1.4.xls'
    workBook = xlrd.open_workbook(excel_url,formatting_info=True)
    workSheet = workBook.sheet_by_name(sheetName)
    dataList = []
    for row in range(startRow-1,endRow):
        reqValue = workSheet.cell_value(row,reqCol)#请求字符串6
        expreValue = workSheet.cell_value(row,expreCol)#预期结果字符串8
        dataList.append((reqValue,expreValue))
    return dataList
if __name__ == '__main__':
    data = get_excelData('1_登录接口',2,5,6,8)
    print(len(data))