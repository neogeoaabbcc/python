#lession_25
#求1+2!+3!+...+20!的和
#-*- UTF-8 -*-
sn = 0
a = 1
b = 0
for b in range(1,21):
    a *= b
    sn += a
    print("1+2!+3!+...+20!= %d" % sn)
