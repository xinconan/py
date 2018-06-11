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

def replaceWithNum(markup):
    spans = markup.findAll('span')
    for span in spans:
        className = span.attrs['class'][0]
        if className == 'numberzero':
            span.replaceWith('0')
        elif className == 'numberone':
            span.replaceWith('1')
        elif className == 'numbertwo':
            span.replaceWith('2')
        elif className == 'numberthree':
            span.replaceWith('3')
        elif className == 'numberfour':
            span.replaceWith('4')
        elif className == 'numberfive':
            span.replaceWith('5')
        elif className == 'numbersix':
            span.replaceWith('6')
        elif className == 'numberseven':
            span.replaceWith('7')
        elif className == 'numbereight':
            span.replaceWith('8')
        elif className == 'numbernine':
            span.replaceWith('9')
        elif className == 'numberdor':
            span.replaceWith('.')

    return markup

# 所有行
trs = table.findAll('tr')
# 处理每一行数据
for tr in trs:
    tds = tr.findAll('td')
    # 第一列是楼栋
    td0 = tds[0].get_text('', strip=True)
    # 房间号
    td1 = tds[1].get_text('', strip=True)
    # 建筑面积
    td2 = replaceWithNum(tds[2].find('a')).get_text().strip()
    # 套内建筑面积
    td3 = replaceWithNum(tds[3].find('a')).get_text().strip()
    # 得房率
    td4 = replaceWithNum(tds[4].find('a')).get_text().strip()
    # 毛坯单价
    td5 = replaceWithNum(tds[5].find('a')).get_text().strip()
    # 装修价
    td6 = replaceWithNum(tds[6].find('a')).get_text().strip()
    # 总价
    td7 = replaceWithNum(tds[7].find('a')).get_text().strip()
    # 可售状态
    td8 = tds[8].get_text('', strip=True)
    print(td0 + ' ' + td1+' '+td2+' '+ td3+' '+td4+' '+td5+' '+td6 + ' '+td7+' '+ td8)
# print(trs)