# auther:shixingjian  time:2020/06/27
import requests
import MySQLdb

def get_course_from_api():
    res = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    return  res.json()['retlist']

def get_course_from_mysql():
    db = MySQLdb.connect(host = '127.0.0.1',user = 'root',passwd = '123456',port = 3306,db = 'plesson',charset = 'utf8')
    cu = db.cursor()
    cu.execute('SELECT * FROM sq_course;')
    data = cu.fetchall()
    cu.close()
    db.close()
    return data

if __name__ == '__main__':
    dbData = get_course_from_mysql()
    apiDate = get_course_from_api()
    # print(dbData,apiDate)
    for ele in dbData:
        print(list(ele))
    for ele in apiDate:
        course_info = ['','','','']#占位符
        i = 0
        for key in ele:
            course_info[i] = ele[key]
            i += 1
        print(course_info)

