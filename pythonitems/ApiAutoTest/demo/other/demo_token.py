#coding=utf8
# auther:shixingjian  time:2020/07/05
import requests
def getToken(userName,passWord):
    header = {"Content-Type":"application/json"}
    payload = f'''
        {{"userName":"{userName}",
          "password":"{passWord}"}}
            '''
    r = requests.post(r"http://47.96.181.17:9090/rest/toController",data= payload, headers = header)
    return r.json()['token']
# getToken('fancl','sq000000')
if __name__ == '__main__':
    getToken('fancl','sq000000')