import requests
def getTokn(username,password):
    header={'Content-Type':'application/json'}
    payload=f'''
    {{"userName":"{username}","password":"{password}"}}
    '''
    # print(payload)
    r=requests.post('http://47.96.181.17:9090/rest/toController',
                    data=payload,
                    headers=header)
    print(r.json())
    return (r.json()['token'])

getTokn('fancl','sq000000')
