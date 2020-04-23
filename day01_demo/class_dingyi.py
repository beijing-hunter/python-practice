class Studen():

    def __init__(self):  # 等同于java中的构造函数，用于初始化对象及属性
        self.name, self.age = "", 0

    def showInfo(self):  # self 等同于java中的this
        print(f"name={self.name},age={self.age}")


class User():
    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(f"name={self.name}")

    def __str__(self):  # 等同于java类中的toString()方法
        return "name=" + self.name

    def __del__(self):  # 等同于java中的析构函数
        print("对象已被删除")


stu = Studen()
stu.name = "tom"
stu.age = 12
stu.showInfo()

u = User("huy")
u.showInfo()
print(u)
