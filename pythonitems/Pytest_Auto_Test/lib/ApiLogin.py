#coding=utf8
# auther:shixingjian  time:2020/07/08
import requests
from config import HOST
import json
class LoginClass:
    def api_login(self,inData,getSession = True):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = json.loads(inData)
        try:
            resp = requests.post(f"{HOST}/api/mgr/loginReq", data=payload, verify=False, headers=header)  # verifi参数绕过HTTPS证书
            resp.encoding = 'unicode_escape'#设置相应编码，显示中文
            if getSession:
                return resp.cookies['sessionid']
            else:
                return resp.json()
        except:
            return {"retcode": 999, "reason": "程序异常"}
if __name__ == '__main__':
    login = LoginClass()
    result = login.api_login('{"username":"auto","password":"sdfsdfsdf"}')
    print(result)