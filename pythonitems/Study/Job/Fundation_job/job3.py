# auther:shixingjian  time:2020/6/24/0024
#1.读取学生信息
file_path = r'd:\shixingjian.txt'
def putInfo(filename):
    resDict ={}
    fo = open(filename)
    lines = fo.read().splitlines()
    for line in lines:
        line = line.replace('(','').replace(')','').replace("'",'').replace(';','')
        temp=line.split(',')
        checktime = temp[0].strip()
        userid = int(temp[1].strip())
        lessensid = int(temp[2].strip())
        # 2.统计排版
        info = {'lessensid':lessensid,'checktime':checktime}
        if userid not in resDict:
            resDict[userid] = [info]
        else:
            resDict[userid].append(info)


        pass
    return resDict

res = putInfo(file_path)

# 3.输出
# print(res)
#完美打印
import pprint
pprint.pprint(res)
