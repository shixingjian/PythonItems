#coding=utf8
# auther:shixingjian  time:2020/07/04
# 新增课程，返回ID，列出课程，循环查看id是否存在、
from lib.courseLib import list_course,add_course
retdict = add_course("物理1","分解机房","12")
if retdict["retcode"] == 0:
    print("测试成功")
    courseID = retdict["id"]
    #查看列表
    retdict2 = list_course(1,500)
    # 循环查看列表id与返回的id是否相等
    for item in retdict2["retlist"]:
        if item["id"] == courseID:
            print("测试成功")