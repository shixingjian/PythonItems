#coding=utf8
# auther:shixingjian  time:2020/07/07
import MySQLdb
def delete_All_Course():
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='plesson', charset='utf8')

    cu = db.cursor()
    cu.execute('delete from sq_course;')
    db.commit()
    # retvalue = cu.fetchone()#返回值
    cu.close()
    db.close()
if __name__ == '__main__':
    retvalues = delete_All_Course()