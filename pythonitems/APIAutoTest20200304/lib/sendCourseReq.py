import json
import time
from lib.courseLib import add,delete,modify,list

def sendCourseReq(row):
    colus5 = json.loads(row[5])  # 请求参数
    retDict = ''
    if (row[4] == 'add'):  # 新增课程
        courseName = colus5['name']
        courseName = courseName.replace('{{courseName}}', '大学物理' + str(int(time.time() * 1000)))
        retDict = add(courseName, colus5['desc'], colus5['display_idx'])
    elif (row[4] == 'delete'):  # 删除课程
        retDict = delete(colus5['id'])
    elif (row[4] == 'list'):  # 列出课程
        retDict = list(colus5['pagenum'], colus5['pagesize'])
    elif (row[4] == 'modidfy'):  # 修改课程
        pass
    else:
        pass

    return retDict

