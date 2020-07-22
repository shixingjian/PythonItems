#coding=utf8
# auther:shixingjian  time:2020/07/04
from lib.courseLib import list_course,add_course
from lib.courseLib import login

# 方法1：新增课程前列出课程信息，数量为N，新增课程后，数量为N+1
sesionid = login("auto","sdfsdfsdf")
# 1.列出课程
retDict1 = list_course(1,500,sesionid)
print(type(retDict1))
# 2.新增课程
retDict2 = add_course("大学生物","aaaaa","85",sesionid)
if retDict2["retcode"] == 0:
    print("测试通过")
else:
    print("测试不通过，课程名称不能相同")
# 3.再次列出课程
retDict3 = list_course(1,500,sesionid)
# 4.比较课程多了一门
if len(retDict3['retlist']) == (len(retDict1['retlist'])+1):
    print('测试通过')

# 新增课程，返回ID，列出课程，循环查看id是否存在