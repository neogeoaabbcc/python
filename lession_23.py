#lession_23
#打印一个菱形图案
#-*- UTF -*-
for i in range(1, 5):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()
for i in range(3,0,-1):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()

for i in range(1, 5):
	print(' ' * (4 - i), end="")
	for j in range(1, 2 * i):
		print('*', end="")
	print()
for i in range(3, 0, -1):
	print(' ' * (4 - i), end="")
	for j in range(1, 2 * i):
		print('*', end="")
	print()
