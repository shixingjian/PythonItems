#coding=utf8
# auther:shixingjian  time:2020/07/06
import requests
# header = {"Content_Type":"application/x-www-form-urlencoded"}
# payload = {
# 			"username":"auto",
# 			"password":"sdfsdfsdf"
# 		}
# resq = requests.post('http://127.0.0.1:9999/api/mgr/loginreq',data=payload)
# resq.encoded = ('unicode_escape')
# print(resq.text)

header = {"Content_Type":"application/json"}
payload = {
			"username":"auto",
			"password":"sdfsdfsdf"
		}
resq = requests.post('http://127.0.0.1:9999/trace/purchase',json=payload)
resq.encoded = ('unicode_escape')
print(resq.text)
