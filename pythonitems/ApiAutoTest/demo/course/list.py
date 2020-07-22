#coding=utf8
# auther:shixingjian  time:2020/07/02
import requests
from config import HOST
dict1 = {"action":"list_course","pagenum":"1","pagesize":"20"}
r = requests.get(f'{HOST}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20',params=dict1)
print(r.text.encode().decode('unicode_escape'))