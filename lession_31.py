#lession_31
#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#-*- UFT-8 -*-
#Monday Tuesday Wednesday Thursday Friday Saturday Sunday
letter = input("请输入星期首字母：\n")
if letter == "S":
    print("请输入第二个字母：")
    letter = input("输入星期第二个字母:\n")
    if letter == "a":
        print("Saturday")
    elif letter == "u":
        print("Sunday")
    else:
        print("日期错误")

elif letter == "F":
    print("Friday")
elif letter == "M":
    print("Monday")
elif letter == "T":
    print("请输入第二个字母：")
    letter = input("输入星期第二个字母:\n")
    if letter == "u":
        print("Tuesday")
    elif letter == "h":
        print("Thursday")
    else:
        print("日期错误")
elif letter == "W":
    print("Wednesday")
else:
    print("日期错误")
