import requests
dict1={'Content-Type':'application/x-www-form-urlencoded'}
payload={
    "username":"auto",
    "password":"sdfsdfsdf"
}
r=requests.post('http://127.0.0.1:80/api/mgr/loginReq',data=payload,headers=dict1)
print(r.json())
print(r.headers)
print(r.cookies['sessionid'])