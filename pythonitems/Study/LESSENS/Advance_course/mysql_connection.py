# auther:shixingjian  time:2020/06/27
import MySQLdb
#打开数据连接
db = MySQLdb.connect()
#获取操作游标
cu = db.cursor()
#通过excute方法执行sql语句
cu.execute('select version();')
#获取执行结果
#fetchne 获取一条结果
#fetchall 获取所有结果
#fetchmany(x) 获取x记录
data = cu.fetchone()
print(data)
#释放资源
cu.close()
db.close()
