import requests
from bs4 import BeautifulSoup
import json

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = 'http://www.tmsf.com/newhouse/property_330184_331788908_price.htm?isopen=1&presellid=12483310&buildingid=&area=&allprice=&housestate=&housetype=1&page='

html = requests.get(url+str(1), headers=headers)
bsObj = BeautifulSoup(html.text, "html.parser")
# table = bsObj.find('div', {'class': 'onbuildshow onbuildshow_contant onbuildshow_contant'})
table = bsObj.select('.onbuildshow .onbuildshow_contant .onbuildshow_contant table')[0]
# 所有行
trs = table.findAll('tr')
# 处理每一行数据
for tr in trs:
    tds = tr.findAll('td')
    # 第一列是楼栋
    td0 = tds[0].get_text().strip()
    print(td0)
# print(trs)