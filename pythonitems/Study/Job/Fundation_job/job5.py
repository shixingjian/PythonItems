# auther:shixingjian  time:2020/06/26
'''
需求分析：
    1- 格式如下----一个file1.txt文件里面内容
        name: Jack   ;    salary:  12000
        name :Mike ; salary:  12300
    2- 格式规范
        每个员工一行，记录了员工的姓名和薪资，
        每行记录 原始文件中并不对齐，中间有或多或少的空格
    3- 计算出所有员工的税后工资（薪资的90%）和扣税明细，
        1- 存入新的文件 file2.txt中
        2- tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数
        3- 输出格式
            name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800

思路分解：
    1- 从文件获取信息 名字 薪资
    2- 计算扣税 排版
    3- 输出文件中
'''
file1Dir = r'D:\file1.txt'
file2Dir = r'D:\file2.txt'
fo1 = open(file1Dir)
fo2 = open(file2Dir,'at')
# print(fo1.read().splitlines())
resList = fo1.read().splitlines()
# print(resList)
newList = []
for one in resList:
    list1 = one.split(';')
    Name = list1[0].strip()
    nameValue = Name.split(':')[1].strip()
    salary = list1[1].strip()
    salaryValue = int(salary.split(':')[1].strip())
    taxValue = round(salaryValue*0.1)
    incomeValue = round(salaryValue - taxValue)
    str = f'name:{nameValue:>6};salary:{salaryValue:>8};tax:{taxValue:>8};income:{incomeValue:>8}\n'
    # newList.append(str)
    fo2.write(str)
# print(newList)
fo1.close()
fo2.flush()
fo2.close()