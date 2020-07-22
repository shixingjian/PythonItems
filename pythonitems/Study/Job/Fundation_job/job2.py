#编写程序，统计出不同类型的文件大小总和
log='''
f20180111151741/i_Ju.jpg    1253
f20180111151741/i_Ju.gif    12530
f20180111151741/i_Ju.jpg    1250
f20180111151741/i_Ju.json    1200
f20180111151741/i_Ju.gif    125
f20180111151741/i_Ju.json    1258
'''
#1.提取每行的文件类型、大小
lines = log.split('\n')
del lines[0],lines[-1] #删除收尾空格，列表之间是制表符\t
#print(lines)
resList = []
for line in lines :
    temp = line.split(' ')
    fileType = temp[0].split('.')[-1]
    fileSize = int(temp[4])
    #print(fileType,fileSize)
    #统计文件类型总和-------[[类型1，大小]，[类型2，大小]]
    #如果文件类型存在，累加大小
    inFlag = False #标志位法--变量来做
    for one in resList: #-----------遍历字列表
        if one[0] == fileType:
            one[1] += fileSize
            inFlag = True
            break#结束循环
    #如果文件类型类型不存在，新增该类型
    if (inFlag == False):
        resList.append([fileType,fileSize])
#print(resList)
for one1 in resList:
    print(one1[0],one1[1])
