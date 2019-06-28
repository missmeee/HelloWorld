
def dayUP(df):
    dayup=1
    for i in range(365):
        if i%4 in [0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor=dayfactor+0.000001
print('工作日努力参数为：{:.6f}'.format(dayfactor))


