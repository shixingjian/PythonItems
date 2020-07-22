#coding=utf8
# auther:shixingjian  time:2020/07/02
import requests
from config import HOST
dict1 = {'Content-Type':'application/json'}
payload = '''
        {
        "action" : "add_course_json",
        "data": {
        "name":"初中英文",
        "desc":"初中化学课程",
        "display_idx":"4"
        }
    }
'''
r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/',headers = dict1,data=payload.encode('utf8'))
print(r.text)