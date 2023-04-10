import pymysql

class save_to_mysql(object):
    def __init__(self):
        self.connect= pymysql.connect(host='192.168.81.1',
                                      user='root',
                                      password='155495',
                                      database='dbtest')
        self.cur = self.connect.cursor()
        print("数据库连接成功")



# ----------------------------------------------


db = pymysql.connect(host='192.168.81.1',
                     user='root',
                     password='155495',
                     database='dbtest')
print(db)
cur = db.cursor()
print(cur)
sql = '''
    	create table t_student(
		no int,
		name varchar(32),
		sex char(1),
		age int(3),
		email varchar(255)
	)

'''
sql2='''
insert into t_student(no,name,sex,age,email) values(1,'zhangsan','m',20,'zhangsan@123.com')

'''
try:
    cur.execute(sql2)
    db.commit()
    print("--------success")

except:
    db.rollback()
    print("fail--------")


