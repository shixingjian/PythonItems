#coding=utf8
# auther:shixingjian  time:2020/07/08
import requests
import json
import pprint
import random
import hashlib
import time
# --------------获取token--------------------
def get_token(userName,passWord):
    token_url = 'http://47.96.181.17:9090/rest/toController'
    payload = {"userName":userName,"password":passWord}
    header = {"Content-Type":"application/json"}
    resp = requests.post(token_url,json=payload,headers=header)
    token_value = json.loads(resp.text)['token']#json---->dict
    return token_value

def get_token2():
    password = hashlib.md5(b'zr111111hg').hexdigest()
    token_url = 'http://121.41.14.39:2001/token/token'
    header = {"Content-Type":"application/x-www-form-urlencoded"}
    payload = {
        "mobile":"13588000000",
        "password":password
    }
    resp = requests.post(token_url,data=payload,headers = header)
    token = resp.json()['data']
    return token


# ----------------------新增客户--------------------
def add_customer(Token):
    # tel = random.randint(00000000,99999999)随机整数
    tel = str(int(time.time() * 1000))[5:]
    add_customer_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
    payload = {
            "aac003": "张三",
            "aac004": "1",
            "aac011": "21",
            "aac030": f"182{tel}",
            "aac01u": "88002255",
            "crm003": "1",
            "crm004": "1",
            "crm00a": "2018-11-11",
            "crm00b": "aaaaaa",
            "crm00c": "2019-02-28",
            "crm00d": "bbbbbb"
            }
    header = {"X-AUTH-TOKEN":Token,"Content-Type":"application/json"}
    resp = requests.post(add_customer_url,json=payload,headers = header)
    return resp.json()


def file_upload(Token):
    file_url = 'http://121.41.14.39:2001/user/doUpload'
    header = {"Content-Type":"multipart/form-data"}
    user_cookie = {"token":Token}
    #文件名字、文件对象、文件类型
    fileloade = {"file":("logo.png",open(r"D:\python\logo.png","rb"),"jpg/png/gif")}
    resp_file = requests.post(file_url,files=fileloade,cookies = user_cookie)
    return resp_file.json()


if __name__ == '__main__':
    # token = get_token('J201903070064',362387359)
    # retinfo = add_customer(token)
    # pprint.pprint(retinfo)#pretyy print完美打印
    pprint.pprint(file_upload(get_token2()))