#lession_34
#练习函数调用
#-*- UTF-8 -*-
def hello_world():
    print("hello world")
def three_world():
    for i in range(3):
        hello_world()

if __name__ == "__main__":
    three_world()
