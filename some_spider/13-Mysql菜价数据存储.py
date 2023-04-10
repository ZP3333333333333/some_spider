"""
connect函数：连接数据库，根据连接的数据库类型不同，该函数的参数也不相同。connect函数返回Connection对象。
cursor方法：获取操作数据库的Cursor对象。cursor方法属于Connection对象。
execute方法：用于执行SQL语句，该方法属于Cursor对象。
commit方法：在修改数据库后，需要调用该方法提交对数据库的修改，commit方法属于Cursor对象。
rollback方法：如果修改数据库失败，一般需要调用该方法进行数据库回滚操作，也就是将数据库恢复成修改之前的样子。
相关操作数据库语句可百度自行查找！！！
"""
from some_spider import pymysql
import requests
import json


def input_page():
    while True:
        try:
            num01 = int(input('输入你要开始爬取的页数：'))
            num02 = int(input('输入你要结束爬取的页数：'))
            if 21079 >= num02 >= num01 > 0:
                return [num01, num02]
            else:
                print('输入的页数不在指定范围内或逻辑出错，请重新输入！')
        except ValueError as f:
            print(f'程序出错: {f}, 请重新输入！')


def get_page(page, url01):
    # 链接数据库(注:db是数据库的名字, connect_timeout连接超时设定)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           password='123456', db='菜价数据库', charset='utf8', connect_timeout=1000)
    # 创建数据库对象
    cursor = conn.cursor()
    sql01 = 'create table if not exists 菜价表 (number varchar(1000), prodCat varchar(1000), prodPcat varchar(8125), ' \
            'prodname varchar(1000), place varchar(1000), highPrice varchar(1000), avgPrice varchar(1000), ' \
            'lowPrice varchar(1000), pubDate varchar(1000)) '
    # 执行创表语句(创建菜价表，并基于字段名和字段对应列的容量)
    cursor.execute(sql01)
    for i in range(page[0], page[1] + 1):
        data = {"current": i}  # 1-21079
        print(f'第{i}页：', data)
        get_url01 = requests.get(url01, data)
        json_text = json.loads(get_url01.text).get('list')  # list中的数据
        for num, i1 in enumerate(json_text):
            prodCat = i1.get('prodCat')  # 一级类
            prodPcat = i1.get('prodPcat')  # 二级类
            prodname = i1.get('prodName')  # 名字
            place = i1.get('place')  # 地区
            highPrice = i1.get('highPrice')  # 最高价
            avgPrice = i1.get('avgPrice')  # 平均价
            lowPrice = i1.get('lowPrice')  # 最低价
            pubDate = i1.get('pubDate')  # 发布日期
            number = (i - 1) * 20 + num + 1
            print(number, prodCat, prodPcat, prodname, place, highPrice, avgPrice, lowPrice,
                  pubDate)
            sql02 = 'insert into 菜价表 (number, prodCat, prodPcat, prodname, place, highPrice, avgPrice, lowPrice, ' \
                    'pubDate) value(%s, %s, %s, %s, %s, %s, %s, %s, %s) '
            # 执行插入表数据语句
            cursor.execute(sql02, (number, prodCat, prodPcat, prodname, place, highPrice, avgPrice, lowPrice, pubDate))
    conn.commit()
    conn.close()


def main():
    page = input_page()
    get_page(page, url)


if __name__ == '__main__':
    # http://www.xinfadi.com.cn/priceDetail.html 原网址
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    main()
