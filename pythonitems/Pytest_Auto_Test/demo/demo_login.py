#coding=utf8
# auther:shixingjian  time:2020/07/08
import requests
HOST = "http://127.0.0.1:80"
def login(userName,passWord):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "username": f"{userName}",
        "password": f"{passWord}"
    }
    resp = requests.post(f"{HOST}/api/mgr/loginReq", data=payload, verify=False, headers=header)  # verifi参数绕过HTTPS证书
    return resp.json()
    # try:
    #     resp = requests.post(f"{HOST}/api/mgr/loginReq", data=payload, verify=False, headers=header)  # verifi参数绕过HTTPS证书
    #     return resp.cookies['sessionid']
    # except:
    #     return {"retcode": 999, "reason": "程序异常"}

if __name__ == '__main__':
    result = login("auto","sdfsdfsdf")
    print(result)