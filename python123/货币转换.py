MoneyStr=input()
if MoneyStr[:3]in['rmb','RMB']:
    usd=eval(MoneyStr[3:])/6.78
    print('USD{:.2f}'.format(usd))
elif MoneyStr[:3]in['USD','usd']:
    rmb=eval(MoneyStr[3:])*6.78
    print('RMB{:.2f}'.format(rmb))
else:
    print('输入格式错误')