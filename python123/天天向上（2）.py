dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1+dayfactor,365)
print('上升：{:.2f},下降：{:.2f}'.format(dayup,daydown))