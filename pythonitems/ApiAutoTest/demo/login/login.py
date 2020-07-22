#coding=utf8
# auther:shixingjian  time:2020/07/03
import requests
from config import HOST
dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
dict2 = {
    "username":"auto",
    "password":"sdfsdfsdf"
}
r = requests.post(f"{HOST}/api/mgr/loginReq",data=dict2)
print(r.text)