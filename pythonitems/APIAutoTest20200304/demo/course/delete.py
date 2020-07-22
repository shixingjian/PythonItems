import requests
from config import HOST

#1.请求头-字典类型
dict1={'Content-Type':'application/x-www-form-urlencoded'}

#2.请求消息体-字典类型
# payload={
#     'action':'delete_course',
#     'id':'2012'
# }

#2.请求消息体-字符串类型
payload="action=delete_course&id=2017"
#3.用requests发送delete请求，data参数如果传入的是字符串，会按原格式发送
r=requests.delete(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=dict1)
print(r.json())

