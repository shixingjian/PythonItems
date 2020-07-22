tel = input('请输入手机号：')
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
def func(str):
    tel1 = ['182','185']
    tel2 = ['151', '152']
    tel3 = ['131', '132']
    temp = str[:3]
    if (temp in tel1):
        return '移动运营商'
    elif (temp in tel2):
        return '电信运营商'
    elif(temp in tel3):
        return '联通运营商'
    else:
        return '不存在该号段'
if len(tel) != 11:
    print('用户位数有误！')

elif (tel.isdigit() is False):
    print('非法字符')
else:
    print(func(tel))
# elif ( int(tel[:2]) == (138 or 139)):
#     print('移动运营商')
# elif (int(tel[0:2]) is (133 or 153)):
#      print('电信运营商')
# elif (int(tel[0:2]) is (130 or 131)):
#     print('联通运营商')
# else:
#     print('不存在该号段')
