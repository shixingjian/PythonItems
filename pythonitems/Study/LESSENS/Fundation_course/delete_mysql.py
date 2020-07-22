# auther:shixingjian  time:2020/06/28
import unittest
import MySQLdb

class TestClassA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "连接数据库，做数据初始化操作"
    def testAdd(self):
        assert 1==1
    @classmethod
    def tearDownClass(cls):
        "连接数据库，做数据清理"
        db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='plesson', charset='utf8')
        cu = db.cursor()
        sql1 = '''
        delete from sq_course 
        where name like '课程%';
        '''
        cu.execute(sql1)
        sql2 = '''
        delete from sq_course 
        where name = 'java';
        '''
        cu.execute(sql2)
        db.commit()
        print("测试成功")
        cu.close()
        db.close()
if __name__ == '__main__':
    #测试加载器
    lo = unittest.TestLoader()
    #测试组
    suite = unittest.TestSuite()
    # 从测试类加载测试用例
    tests = lo.loadTestsFromTestCase(TestClassA)
    # 将测试用例加载到测试组
    suite.addTests(tests)
    # ;运行测试用例
    unittest.TextTestRunner(verbosity=2).run(suite)

    # unittest.defaultTestLoader.discover()

    # unittest.main()

