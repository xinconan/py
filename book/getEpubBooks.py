# 获取图灵电子书目录

import requests
import math
import time

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Host': 'www.epubit.com',
    'Origin': 'https://www.epubit.com',
    'Referer': 'https://www.epubit.com/book/screen?flagBookType=2',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'https://www.epubit.com/book/search'

data = {
    'page':1,
    'rows':12,
    'searchColumn':'',
    'eleEdPrice':'',
    'categoryId':'',
    'order':'desc',
    'sort':'ebookShelvesDate',
    'listed':1,
    'isEbook':1
}

totalPage = 60
pageNum = 1
ebookList = []

def getPage():
    resp = requests.post(url,data=data, headers=headers)
    result = resp.json()
    total = result['data']['total']
    list = result['data']['rows']
    global  totalPage
    totalPage = math.ceil(total / 12)
    return list

while pageNum <= totalPage:
    print('正在获取第' + str(pageNum)+'页数据')
    ebookList += getPage()
    pageNum += 1
    data['page'] = pageNum
    time.sleep(1)  # 休眠1秒

for book in ebookList:
    print(book['name'])