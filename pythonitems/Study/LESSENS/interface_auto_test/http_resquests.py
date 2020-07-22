#coding=utf8
# auther:shixingjian  time:2020/07/02
# -----------------访问百度首页---------------
import requests

a = requests.get("http://www.baidu.com")
a.encoding='utf8'
print(a.text) #获取相应体文本


# -----------获取课程列表----------------
#r为响应消息，r.text表示响应消息体的文本格式
# r = requests.get('http://localhost:80/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
# print(r.text)

#action=list_course&pagenum=1&pagesize=20
# payload = {"action":"list_course",
#            "pagenum":1,
#            "pagesize":20
#             }
# r = requests.get("http://localhost:80/api/mgr/sq_mgr/",params=payload)
# print(r.text)

# -------------新增课程----------------
# dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
# payload = {
#         "action":"add_course",
#         "data":'''
#         {"name":"初中化学","desc":"初中化学课程","display_idx":4}'''
#
# }
# r = requests.post("http://localhost:80/api/mgr/sq_mgr/",headers = dict1,data = payload)
# print(r.text.encode().decode('unicode_escape'))#先检查text什么类型，str类型：str.encode().decode(unicode_escape);bytes类型：text.decode('unicode_escape')
#r.text 文本响应内容--后去网页HTML
#r.content 字节响应内容--下载图片或文件
#r.raw 原始响应内容----不用
#r.json() 字典响应内容


# ---------------新增课程2---------------
# dict1 = {'Content-Type':'application/json'}
# payload = '''
#         {
#         "action" : "add_course_json",
#         "data": {
#         "name":"初中英文",
#         "desc":"初中化学课程",
#         "display_idx":"4"
#         }
#     }
# '''
# r = requests.post('http://localhost/apijson/mgr/sq_mgr/',headers = dict1,data=payload.encode('utf8'))
# print(r.text)

# -----------用户登录--------------
# dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
# dict2 = {
#     "username":"auto",
#     "password":"sdfsdfsdf"
# }
# r = requests.post("http://localhost/api/mgr/loginReq",data=dict2)
# print(r.text)

# ------------新增课程（json格式）----------------
# dict1 = {'Content-Type':'application/json'}
# dict2 = {
#     "action": "add_course_json",
#     "data": {
#         "name": "初中化学",
#         "desc": "初中化学课程",
#         "display_idx": "4"
#     }
# }
# r = requests.post("http://localhost/apijson/mgr/sq_mgr/",json=dict2)
# print(r.text)

# print(r.status_code)#响应码
# print(r.headers)#响应头
# print(r.headers['Set-Cookie'])#获取cookie
# print(r.cookies)#获取cookie
# print(r.cookies['sessionid'])#获取session
# print(r.headers['Content-Type'])#获取content-type

