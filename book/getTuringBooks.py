# 获取图灵电子书目录

import requests
from bs4 import BeautifulSoup
import json

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

url = 'http://www.ituring.com.cn/book?tab=ebook&sort=new&page='
pageNum = 34   # 总共的页数

# 获取每页的数据
def getPage(page):
    print('正在获取第' + str(page) + '页数据')
    html = requests.get(url+str(page-1), headers=headers)
    bsObj = BeautifulSoup(html.text, "html.parser")

    ebookList = [];
    ebook = bsObj.findAll('div',{'class': 'block-books block-books-grid'})[0].findAll('li');

    for item in ebook:
        bookItem = item.find('div',{'class':'book-img'}).find('a')
        # list = {
        #     'title':bookItem.attrs['title'],
        #     'url': 'http://www.ituring.com.cn'+bookItem.attrs['href'],
        #     'img':bookItem.find('img').attrs['src']
        # }
        # ebookList.append(list)
        ebookList.append(bookItem.attrs['title'])

    return ebookList

lists = []
# 循环遍历获取每页数据
for num in range(1, pageNum + 1):
    lists += getPage(num)


for book in lists:
    print(book)
