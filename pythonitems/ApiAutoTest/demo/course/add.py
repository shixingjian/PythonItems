#coding=utf8
# auther:shixingjian  time:2020/07/02
import requests
from config import HOST
dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {
        "action":"add_course",
        "data":'''
        {"name":"初中化学","desc":"初中化学课程","display_idx":4}'''
}
r = requests.post(f"{HOST}/api/mgr/sq_mgr/",headers = dict1,data = payload)
print(r.text.encode().decode('unicode_escape'))