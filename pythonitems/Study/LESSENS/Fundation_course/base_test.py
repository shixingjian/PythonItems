# auther:shixingjian  time:2020/6/25/0025
import re
res = re.findall("s.",'songqinsis')#需要两个必填参数（正则表达式，处理的字符串）2.返回类型，列表
print(res)
res = re.findall('s*','songqinsin')#允许模式出现0次或多次
print(res)
res = re.findall('s+','songqinsin')#允许模式出现1次或多次
print(res)
res = re.findall('son*','songqinso')
print(res)
res = re.findall('song+','songqin')
print(res)


