import requests
from config import HOST

#1.请求消息体-字典类型
payload={'action':'list_course','pagenum':1,'pagesize':20}
#2.用requests发送get请求，params参数只有get请求才有
r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload)
#3.响应消息体内容转为utf-8编码
r.encoding="utf-8"

print(r.text)

