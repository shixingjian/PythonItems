from lib.courseLib import add,list
import time
from lib.loginLib import  login
#1.新增一个系统中不存在的课程
sessionid=login('auto','sdfsdf')
courseName='初中化学'+ str(int(time.time()*10000))
retDict=add(courseName,'sdfdss',0)
print(retDict)

if retDict['retcode']==0:
    print('>>>>>新增课程测试通过')
    id=retDict['id']
    #2.调用列出课程接口，查看新增的课程是否存在
    retDict2=list(1,500)
    # print(retDict2['retlist'])
    exit2=0
    for item in retDict2['retlist'] :
        if id==item['id'] :
            print('>>>>>列出课程测试通过')
            exit2 = 2
            break
    if exit2==0:
        print('>>>>>列出课程测试不通过')
else:
    print('>>>>>>测试不通过')