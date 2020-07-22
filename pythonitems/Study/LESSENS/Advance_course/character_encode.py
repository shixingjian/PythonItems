# auther:shixingjian  time:2020/06/28
# print(ord("你"))#字符---整数，一个字符
# print(chr(20320))#整数---字符

# a = 'abc'
# b = b'abc'指定abc为bytes类型
# b = b''指定空的bytes类型
# print(type(a))
# print(type(b))

# with open(r'F:\pycharm\project\Study\File\a.txt','w',encoding='utf8') as f :
#     f.write("大丈夫何患无妻")

# with open(r'F:\pycharm\project\Study\File\a.txt','r',encoding='utf8') as f :
#     print(f.read())

#以字节流bytes写
# with open(r'F:\pycharm\project\Study\File\b.txt','wb') as f:
#     f.write("人".encode('big5'))

#以字节流bytes读
# with open(r'F:\pycharm\project\Study\File\b.txt','rb') as f:
#     print(f.read().decode('big5'))

#初始化空数据
# photoData = b''
#二进制模式读
# with open(r'F:\pycharm\project\Study\File\photo.jpg','rb') as f:
#     photoData = f.read()
# # 二进制模式写
# with open(r'F:\pycharm\project\Study\File\photo1.jpg','wb') as f:
#     f.write(photoData)

import chardet

def get_encoding(file):
    with open(file,'rb') as f:
        data = f.read()
        return chardet.detect(data)#返回文件编码、数据信息
resb = get_encoding(r'F:\pycharm\project\Study\File\a.txt')
print(resb)#编码类型/相似度

