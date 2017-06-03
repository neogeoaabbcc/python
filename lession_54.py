#lession_54
#取一个整数a从右端开始的4〜7位。
#-*- UTF-8 -*-

if __name__ == "__main__":
    a = int(input("请输入一个数字：\n"))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print("%o\t%o" % (a,d))
