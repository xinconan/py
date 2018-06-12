import requests
from bs4 import BeautifulSoup
import xlsxwriter

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = 'http://www.tmsf.com/newhouse/property_330184_331788908_price.htm?isopen=1&presellid=12483310&buildingid=&area=&allprice=&housestate=1&housetype=1&page='

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

# 获取每页的数据
def getPage(page):
    print('正在获取第' + str(page) + '页数据')
    html = requests.get(url+str(page), headers=headers)
    bsObj = BeautifulSoup(html.text, "html.parser")
    # table = bsObj.find('div', {'class': 'onbuildshow onbuildshow_contant onbuildshow_contant'})
    table = bsObj.select('.onbuildshow .onbuildshow_contant .onbuildshow_contant table')[0]
    # 所有行
    trs = table.findAll('tr')

    list = []

    # 处理每一行数据
    for tr in trs:
        tds = tr.findAll('td')
        # 楼栋
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

        td = {
            'building': td0,
            'room': td1,
            'area': td2,
            'areaIn': td3,
            'rate': td4,
            'price': td5,
            'decoratePrice': td6,
            'totalPrice': td7,
            'status': td8
        }
        list.append(td)

    print('第' + str(page) + '页数据获取成功')
    return list

houseList = []
pageNum = 48  # 1-48
for num in range(1, pageNum + 1):
    houseList += getPage(num)

print('正在将数据保存到文件中')

filename = '万科未来城三期.xlsx'
wb = xlsxwriter.Workbook(filename)
sheet = wb.add_worksheet('三期')
bold = wb.add_format({'bold': True})
# 生成表头
title = ['楼栋', '房号', '建筑面积', '套内建筑面积', '得房率', '申请毛坯单价', '装修价', '总价', '状态']

col = 0
for head in title:
    sheet.write(0, col, head, bold)
    col += 1

row = 1 # 从第1行开始
for item in houseList:
    sheet.write(row, 0, item['building'])
    sheet.write(row, 1, item['room'])
    sheet.write(row, 2, item['area'])
    sheet.write(row, 3, item['areaIn'])
    sheet.write(row, 4, item['rate'])
    sheet.write(row, 5, item['price'])
    sheet.write(row, 6, item['decoratePrice'])
    sheet.write(row, 7, item['totalPrice'])
    sheet.write(row, 8, item['status'])
    row += 1

wb.close()
print('done!')