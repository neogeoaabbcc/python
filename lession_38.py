#lession_37
#求一个3*3矩阵对角线元素之和。
#-*- UTF-8 -*-

if __name__ == "__main__":

    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("输入一个数字：\n")))

    for i in range(3):
        sum += a[i][i]
    print(sum)
