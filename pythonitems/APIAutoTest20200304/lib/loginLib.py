
def login(username,password):
    import requests
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "username": username,
        "password": f"{password}"
    }
    try:
        r = requests.post('http://localhost/api/mgr/loginReq', data=payload, headers=dict1)
        return r.cookies['sessionid']
    except:
        return '11111111'

sessionid=login('auto','sdfsdfsdf')
print(sessionid)