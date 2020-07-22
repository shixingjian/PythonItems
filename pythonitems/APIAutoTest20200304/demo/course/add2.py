import requests
from config import HOST

#1.请求头-字典类型
dict1={'Content-Type':'application/json'}

#2.请求消息体-字符串类型
payload='''
{
  "action" : "add_course_json",
  "data"	: {
    "name":"初中化22学",
    "desc":"初中化学课程",
    "display_idx":"4"
  }
}
'''
payload=payload.encode(encoding='utf-8')

#3.用requests发送post请求，data参数如果传入的是字符串，会按原格式发送
r=requests.post(f'{HOST}/apijson/mgr/sq_mgr/',data=payload,headers=dict1)

print(r.text)







