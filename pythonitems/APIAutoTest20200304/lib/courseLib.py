import requests
from config import HOST

#1.定义新增课程函数
def add(name,desc,display_idx,sessionID):
    #请求头
    sessionID='sessionid='+sessionID
    dict1={'Content-Type':'application/x-www-form-urlencoded','Cookie':sessionID}
    #消息体
    payload={
        'action':'add_course',
        'data':f'{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'
    }
    cookie={"sessionid":sessionID}
    try:
        r=requests.post(f'{HOST}/api/mgr/sq_mgr/',verify=False,data=payload,headers=dict1,cookies=cookie)
        return r.json()
    except:
        return {"retcode": 999, "reason": '程序异常'}

#2.定义删除课程函数
def delete(id,sessionID):
    cookie = {"sessionid": sessionID}
    # 请求头
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    # 消息体
    payload={
        'action':'delete_course',
        'id':id
    }
    try:
        r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', verify=False,data=payload, headers=dict1,cookies=cookie)
        return r.json()
    except:
        return {"retcode": 999, "reason": '程序异常'}

#3.定义修改课程函数
def modify(id,name,desc,display_idx,sessionID):
    cookie = {"sessionid": sessionID}
    # 请求头
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    # 消息体
    payload = {
        'action': 'modify_course',
        'id': id,
        'newdata': f'''{{"name":"{name}","desc":"{desc}",
                          "display_idx":"{display_idx}"
                        }}'''
    }
    try:
        r = requests.put(f'{HOST}/api/mgr/sq_mgr/', verify=False,data=payload, headers=dict1,cookies=cookie)
        return r.json()
    except:
        return {"retcode": 999, "reason": '程序异常'}

#4.定义列出课程函数
def  list(pagenum,pagesize,sessionID):
    cookie = {"sessionid": sessionID}
    payload = {'action': 'list_course', 'pagenum': pagenum, 'pagesize': pagesize}
    try:
        r = requests.get(f'{HOST}/api/mgr/sq_mgr/', verify=False,params=payload,cookies=cookie)
        r.encoding = "utf-8"
        return r.json()
    except:
        return {"retcode": 999, "reason": '程序异常'}

#5.定义新增课程2函数
def add2(name,desc,display_idx,sessionID):
    cookie = {"sessionid": sessionID}
    # 请求头
    dict1 = {'Content-Type': 'application/json'}
    # 消息体
    payload = f'''
    {{
      "action" : "add_course_json",
      "data"	: {{
        "name":"{name}",
        "desc":"{desc}",
        "display_idx":"{display_idx}"
      }}
    }}
    '''

    try:
        payload = payload.encode(encoding='utf-8')
        r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/',verify=False, data=payload, headers=dict1,cookies=cookie)
        return r.json()
    except:
        return {"retcode": 999, "reason": '程序异常'}





