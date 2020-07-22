#coding=utf8
# auther:shixingjian  time:2020/07/02
import requests
from config import HOST
dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
payload={"action":"delete_course","id":"5"}
r = requests.delete(f"{HOST}/api/mgr/sq_mgr/",headers = dict1,data = payload)
print(r.json())