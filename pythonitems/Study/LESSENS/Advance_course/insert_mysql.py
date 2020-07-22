# auther:shixingjian  time:2020/06/28
import MySQLdb
db = MySQLdb.connect(host = '127.0.0.1',port = 3306,user = 'root',passwd = '123456',db = 'plesson',charset = 'utf8')
cu = db.cursor()
# cu.execute("insert into sq_course value(4,'java','java数据',4);")
# 一次性插入多条数据
# sql = '''
# insert into sq_course(name,`desc`,display_idx)
# values ("课程7","课程7的描述","1"),
#        ("课程8","课程8的描述","1"),
#        ("课程9","课程9的描述","1"),
#        ("课程10","课程10的描述","1"),
#        ("课程11","课程11的描述","1");
# '''
#插入多条数据
def insert_date(start,end):
    sql1 = "insert into sq_course(name,`desc`,display_idx) values"
    sql2 = ''
    for i in range(start,end+1):
        if i == end:
            sql2 += f'("课程{i}","课程{i}的描述","1");'
        else:
            sql2 += f'("课程{i}","课程{i}的描述","1"),\n'
    return sql1 + sql2
sql = insert_date(12,16)
cu.execute(sql)
db.commit()#数据库修改都要提交到数据库update---set--，delete from,insert into
#获取返回值
data = cu.fetchone()#没有返回值
print(data)
cu.close()
db.close()

