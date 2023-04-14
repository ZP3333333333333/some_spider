import requests
import re
import csv
import pymysql


def getPackageName(pageSize, curPage):
    db = pymysql.connect(host='192.168.81.1',
                         user='root',
                         password='155495',
                         database='dbtest')
    print("数据库连接成功")
    cur = db.cursor()
    sql = '''
        	create table t_package(
    		name varchar(50),
    		version varchar(32)
    	)

    '''
    sql2 = '''
    insert into t_student(no,name,sex,age,email) values(1,'zhangsan','m',20,'zhangsan@123.com')
    '''
    # if curPage == 1:
    #     cur.execute(sql)

    url = '''https://repo.harmonyos.com/hpm/registry/api/bundles?condition={"orderBy":[{"field":"downloads","orderType":"DESC"}],"matchBy":[{"field":"name","opt":"CONTAIN","value":""}]}
    ''' + f'''&pageSize={pageSize}&curPage={curPage}'''
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text

    obj = re.compile(r'{"name":"@.*?/(?P<name>.*?)","version":"(?P<version>.*?)","rom":')
    result = obj.finditer(page_content)

    for it in result:
        # print(it.group("name"))
        # print(it.group("version"))
        name = it.group("name")
        version = it.group("version")
        sql2 = '''
        insert into official_package(name,version) values(%s,%s)
        '''
        cur.execute(sql2, (name, version))
    print("get one page success\n")
    db.commit()
    db.close()


if __name__ == '__main__':

    for i in range(1, 50):
        getPackageName(20, i)

# print(page_content)
