# auther:shixingjian  time:2020/06/28
import requests
data = [
    {"action":"add_course","data":'{"name":"课程1","desc":"01","display_idx":"1"}'},
    {"action":"add_course","data":'{"name":"课程2","desc":"02","display_idx":"1"}'},
    {"action":"add_course","data":'{"name":"课程3","desc":"03","display_idx":"1"}'},
    {"action":"add_course","data":'{"name":"课程4","desc":"04","display_idx":"1"}'},
    {"action":"add_course","data":'{"name":"课程5","desc":"05","display_idx":"1"}'},
    {"action":"add_course","data":'{"name":"课程6","desc":"06","display_idx":"1"}'},
]
#一行代码实现接口请求，一次性传100个数据
reslist = [requests.post("http://localhost/api/mgr/sq_mgr/",data = i) for i in data] #列表生成式
for res in reslist:
    print(res.text)