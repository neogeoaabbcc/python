#lession_6
#斐波那契数列。
#-*-UTF-8-*-
def Feb(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
print(Feb(10))
