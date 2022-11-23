'''
dayup = pow(1.001, 365)
daydown = pow(1 - 0.001, 365)

print("Make progress every day{:.2f}, otherwise:{:.2f}".format(dayup, daydown))
'''

'''
one_year = 365
dayfactor = 0.01

dayup = pow(1 + dayfactor, one_year)
daydown = pow(1 - dayfactor, one_year)
print("make progres every day:{:.2f}, otherwise:{:.2f}".format(dayup,daydown))
'''

'''
#工作日每天进步1%，休息日每天退步1%
#计算周末的算法：365模7余0为周日余6位周六
dayup = 1.0
factor = 0.01

for i in range(365):
    if i % 7 in [0, 6]:
        dayup = dayup * (1 - factor)
    else:
        dayup = dayup * (1 + factor)
print("work time{:.2f}".format(dayup))
'''

'''
#数学思维 - 》 计算思维（直接试错）
#grit is very important
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i  % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup

dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print(dayfactor)
'''

