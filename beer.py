# 青岛啤酒活动，联通每天领3次共90M流量
# https://www.52pojie.cn/thread-950775-1-1.html
import requests as r
import time


def f1(num):
    data1 = {
        'phoneVal': num,
        'type': '21'
    }
    # 获取验证码
    print(r.post('https://m.10010.com/god/AirCheckMessage/sendCaptcha', data=data1).text)

    # 领取流量
    print(r.get('https://m.10010.com/god/qingPiCard/flowExchange?number=%s&type=21&captcha=%s' % (
    num, input('验证码: ').strip())).text)


phonenumber = input("请输入手机号：")

for i in range(3):
    print('==第{}次领取=='.format(i + 1))
    f1(phonenumber)
    if i == 2:
        print('今天已经领完啦！请明天再来吧。')
        print('程序将在5s后退出。。。')
        time.sleep(65)
    else:
        print('请等待65s后面还有{}次哦'.format(2 - i))
        time.sleep(65)