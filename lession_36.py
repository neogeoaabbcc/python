#lession_36
#求100之内的素数。
#-*- UFT-8 -*-

lower = int(input("请输入最小数字"))
upper = int(input("请输入最大数字"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
