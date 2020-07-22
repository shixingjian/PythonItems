import requests
from config import HOST

#1.请求头-字典类型
dict1={'Content-Type':'application/x-www-form-urlencoded'}
#2.请求消息体-字典类型
payload={
    'action':'modify_course',
    'id':'2013',
    'newdata': '''{"name":"初中化学8888","desc":"初中化学课程",
                      "display_idx":"4"
                    }'''
}
#3.用requests发送put请求，data参数如果传入的是字典，会自动转换为表单
r=requests.put(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=dict1)
print(r.json())



