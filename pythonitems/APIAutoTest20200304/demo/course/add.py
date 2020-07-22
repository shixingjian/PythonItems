import requests
from config import HOST

#1.请求头-字典类型
dict1={'Content-Type':'application/x-www-form-urlencoded'}

#2.请求消息体-字典类型
payload={
    'action':'add_course',
    'data':'{"name":"ssss","desc":"bbb","display_idx":"4"}'
}
#3.用requests发送post请求，data参数如果传入的是字典，会自动转换为表单
r=requests.post(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=dict1)
print(r.text)


