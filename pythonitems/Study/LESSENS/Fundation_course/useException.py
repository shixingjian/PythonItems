# auther:shixingjian  time:2020/6/25/0025
class NameLongError(Exception):
    err = 'name.long'
    #print('namelongerror')
    def methFun(self):
        pass
class NameShortError(Exception):
    err = 'name.short'
    #print('nameshorterror')

def inputNmae():
    name = input('请输入用户名：')
    if len(name) >10:
        raise NameLongError
    elif len(name) < 5:
        raise NameShortError
try :
    inputNmae()
except NameShortError as e:
    print("您输入的用户名过短",e.err)
except NameLongError as e:
    print('您输入的用户名过长',e.err)
    e.methFun()