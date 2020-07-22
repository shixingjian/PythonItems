#coding=utf8
# auther:shixingjian  time:2020/07/02
import requests
from config import HOST
# -----------新增课程-------------
def add_course(name,desc,display_idx,sesionID):
    dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
    dict2 = {"sessionid": sesionID}
    payload = {
            "action":"add_course",
            "data":f'''
            {{"name":"{name}","desc":"{desc}","display_idx":{display_idx}}}'''
    }
    try:
        r = requests.post(f"{HOST}/api/mgr/sq_mgr/",verify = False,headers = dict1,data = payload,cookies = dict2)
        # print(r.text.encode().decode('unicode_escape'))
        return r.json()
    except:
        return {"retcode":999,"reason":"程序异常"}

def add2_course(name,desc,display_idx,sesionID):
    dict1 = {'Content-Type': 'application/json'}
    dict2 = {"sessionid": sesionID}
    payload = f'''
            {{
            "action" : "add_course_json",
            "data": {{
            "name":"{name}",
            "desc":"{desc}",
            "display_idx":"{display_idx}"
            }}
        }}
    '''
    try:
        r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/',verify = False,headers=dict1, data=payload.encode('utf8'),cookies = dict2)
        return r.json()
    except:
        return {"retcode":999,'reason':'程序异常'}


# -----------删除课程-------------
def delete_course(id,sesionID):
    dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
    dict2 = {"sessionid": sesionID}
    payload={"action":"delete_course","id":id}
    try:
        r = requests.delete(f"{HOST}/api/mgr/sq_mgr/",verify = False,headers = dict1,data = payload,cookies = dict2)
        return r.json()
    except:
        return {"retcoede":999,"reason":"程序异常"}

# -----------修改课程-------------
def modify_course(id,name,desc,display_idx,sesionID):
    dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
    dict2 = {"sessionid": sesionID}
    payload = {"action": "modify_course", "id":id, "newdata":
             f'''
            {{"name":"{name}",
            "desc":"{desc}",
            "display_idx":"{display_idx}"}}
            '''
        }
    try:
        r = requests.put(f"{HOST}/api/mgr/sq_mgr/",verify = False,headers = dict1,data=payload,cookies = dict2)
        return r.json()
    except:
         return {"retcode":999,"reason":"程序异常"}

# -----------查询课程-------------
def list_course(pagenum,pagesize,sesionID):
    dict1 = {"action": "list_course", "pagenum": pagenum, "pagesize":pagesize}
    dict2 = {"sessionid":sesionID}
    try:
        r = requests.get(f'{HOST}/api/mgr/sq_mgr/', verify = False,params=dict1,cookies = dict2)
        return r.json()
    except:
        return {"retcode":999,"reason":"程序异常"}

# -----------用户登录-------------
def login(username,password):
    dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
    dict2 = {
        "username":f"{username}",
        "password":f"{password}"
    }
    try:
        r = requests.post(f"{HOST}/api/mgr/loginReq",data=dict2,verify = False,headers = dict1)#verifi参数绕过HTTPS证书
        return r.cookies['sessionid']
    except:
        return {"retcode":999,"reason":"程序异常"}

if __name__ == '__main__':
    a = login("auto","sdfsdfsdf")
    print(a)
