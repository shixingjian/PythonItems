#coding=utf8
# auther:shixingjian  time:2020/07/08
import requests
from config import HOST
import json
class LessonClass:
    #1.新增课程
    def add_lesson(self,session,inData):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        cookie = {"sessionid": session}
        payload = {
            "action": "add_course",
            "data": inData
        }
        try:
            r = requests.post(f"{HOST}/api/mgr/sq_mgr/", verify=False, headers=header, data=payload, cookies=cookie)
            # print(r.text.encode().decode('unicode_escape'))
            return r.json()
        except:
            return {"retcode": 999, "reason": "程序异常"}
    #2.列出课程
    def list_lesson(self,session,inData):
        payload = inData#dict
        cookie = {"sessionid": session}
        try:
            r = requests.get(f'{HOST}/api/mgr/sq_mgr/', verify=False,
                             params=payload, cookies=cookie)
            return r.json()
        except:
            return {"retcode": 999, "reason": "程序异常"}
    #3.修改课程
    def modify_lesson(self,session,id,inDate):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        cookie= {"sessionid": session}
        payload = {"action": "modify_course", "id": id, "newdata":json.dumps(inDate)}
        try:
            r = requests.put(f"{HOST}/api/mgr/sq_mgr/", verify=False, headers=header, data=payload, cookies=cookie)
            return r.json()
        except:
            return {"retcode": 999, "reason": "程序异常"}
    #4.删除课程
    def delete_lesson(self,session,inData):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        cookie = {"sessionid": session}
        payload = inData#dict
        try:
            r = requests.delete(f"{HOST}/api/mgr/sq_mgr/", verify=False, headers=header, data=payload, cookies=cookie)
            return r.json()
        except:
            return {"retcoede": 999, "reason": "程序异常"}
