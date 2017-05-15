#lession_12
#-*- UTF-8 -*-
#判断101-200之间有多少个素数，并输出所有素数。
h=0
leap=1
from math import sqrt
from sys import stdout
for i in range(101,201):
    k=int(sqrt(i+1))
    for j in range(2,k+1):
        if i%j==0:
            leap=0
            break
    if leap == 1:
        print("%d" % i)
        h+=1
        if h%10==0:
            print("")

    leap=1

print("The total is %d" % h)
