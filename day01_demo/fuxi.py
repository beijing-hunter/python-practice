name = "tom"
age = 12
tz = 12.3
print("我是：%s,今年：%d,体重：%.2f" % (name, age, tz))

valueStr = input("请输入值：")
value = eval(valueStr)

print("你输入的数据类型是：%s,值为：%s" % (type(value), value))

list5 = [i for i in range(10)]
print(list5)

list5 = [i for i in range(20) if i % 2 == 0]
print(list5)

dict3 = {key: key ** 2 for key in range(10)}
print(dict3)

dict4 = {key: value for key, value in dict3.items() if key > 5}
print(dict4)


def addSum(v1, v2):
    return v1 + v2

def showMessage():
    """显示信息"""
    value = addSum(12, 23)
    print(value)
    return "hello world"


print(help(showMessage))  # 查看函数说明文档
print(showMessage())


class Student():
    def __init__(self):
        self.name, self.age, self.tz = '', 0, 0.00

    def showInfo(self):
        return self.name + ":" + str(self.age) + ":" + str(self.tz)


stu = Student()
stu.name = 'tom'
stu.age = 130
stu.tz = 12.3
print(stu.showInfo())
