from requests_html import HTMLSession
session = HTMLSession()
r=session.get('http://finance.sina.com.cn/forex/cny.shtml')
r.html.render()
hl = r.html.find('#divHSZS > ul:nth-child(1) > li:nth-child(2)', first=True)
print('当前汇率为：',hl.text)
MoneyStr=input('请以按格式输入需要换算的货币：')
if MoneyStr[:3]in['rmb','RMB']:
    usd=eval(MoneyStr[3:])/float(hl.text)
    print('USD{:.4f}'.format(usd))
elif MoneyStr[:3]in['USD','usd']:
    rmb=eval(MoneyStr[3:])*float(hl.text)
    print('RMB{:.4f}'.format(rmb))
else:
    print('输入格式错误')