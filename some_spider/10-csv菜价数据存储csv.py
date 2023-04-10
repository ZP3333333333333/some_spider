import requests
import json
# 采用了csv库的写入方式
import csv


# 获取爬取页数的范围
def input_page():
    # 循环输入防止输入不正规
    while True:
        try:
            num01 = int(input('输入你要开始爬取的页数：'))
            num02 = int(input('输入你要结束爬取的页数：'))
            # 通过网页可以发现最大页数是21079，也可以自己再另外请求得到最大页数(这里不做展示)
            if 21079 >= num02 >= num01 > 0:
                return [num01, num02]
            else:
                print('输入的页数不在指定范围内或逻辑出错，请重新输入！')
        except ValueError as f:
            print(f'程序出错: {f}, 请重新输入！')


# ger请求得到的页数并保存csv数据
def get_page(page, url01):
    # 代码设置为a追加模式, 不会重写文件, 如果不添加newline=''的话保存的数据会有空一行
    # 如有编码问题, 请更改encoding
    with open('./北京新发地菜价.csv', 'a', encoding='gbk', newline='') as f:
        a = csv.writer(f)
        # 字段存储一次就行，无需放到循环体中
        field = ['序号', '一级类', '二级类', '名字', '地区', '最高价', '平均价', '最低价', '发布日期']
        a.writerow(field)
        print(['序号', '一级类', '二级类', '名字', '地区', '最高价', '平均价', '最低价', '发布日期'])
        # 遍历输入的页数
        for i in range(page[0], page[1] + 1):
            data = {"current": i}  # 1-21079
            print(f'第{i}页：', data)
            # 通过网页观察发现添加data数据，就能拿到对应的页数的数据
            get_url01 = requests.get(url01, data)
            # 将get的数据转化为json格式并获取到里面的list部分
            json_text = json.loads(get_url01.text).get('list')
            # 遍历每一页中获得对应的数据
            for num, i1 in enumerate(json_text):
                prodCat = i1.get('prodCat')  # 一级类
                prodPcat = i1.get('prodPcat')  # 二级类
                prodname = i1.get('prodName')  # 名字
                place = i1.get('place')  # 地区
                highPrice = i1.get('highPrice')  # 最高价
                avgPrice = i1.get('avgPrice')  # 平均价
                lowPrice = i1.get('lowPrice')  # 最低价
                pubDate = i1.get('pubDate')  # 发布日期
                # 写入csv
                list_data = [(i - 1) * 20 + num + 1, prodCat, prodPcat, prodname, place, highPrice, avgPrice, lowPrice,
                             pubDate]
                print(list_data)
                a.writerow(list_data)


def main():
    page = input_page()
    get_page(page, url)


if __name__ == '__main__':
    # http://www.xinfadi.com.cn/priceDetail.html  # 原网址
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    main()
