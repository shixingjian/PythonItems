from lib.courseLib import add,list
import time
#1.新增一个系统中不存在的课程
courseName='初中化学'+ str(int(time.time()*10000))
retDict9=add(courseName,'sdfdss',0)
# 再次新增一样的课程
retDict=add(courseName,'sdfdss',0)

print(retDict)

if retDict['retcode']==2:
    print('>>>>>新增同名课程测试通过')
    #2.调用列出课程接口，查看新增的课程是否存在
    retDict2=list(1,500)
    # print(retDict2['retlist'])
    exit2=0
    for item in retDict2['retlist'] :
        if courseName==item['name'] :
            exit2 = exit2+1
    if exit2>1:
        print('>>>>>列出课程测试不通过')
    elif  exit2==1:
        print('>>>>>列出课程测试通过')
else:
    print('>>>>>>测试不通过')