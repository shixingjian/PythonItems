#coding=utf8
# auther:shixingjian  time:2020/07/05
import base64
str = 'shixingjian'
enstr = base64.b64encode(str.encode('utf8'))
print('编码后的结果',enstr)
bstr = base64.b64decode(enstr)
print('编码后的字节码',bstr)
print('编码后的结果',bstr.decode("utf8"))



