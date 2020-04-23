class Persion():
    def __init__(self):
        self.__address = "北京市朝阳区"  # 私有属性，不被对外访问
        self.xingshi = "胡"

    def getAddress(self):
        return self.__address

    def __createXS(self):  # 私有方法
        datas = ["刘", "胡", "李"]
        return datas[0]


class School():
    def __init__(self):
        self.name = "北京十七中学"

    def __str__(self):
        return "学校名称:" + self.name


class Student(Persion, School):
    pass


stu = Student()
print(stu.xingshi)
print(Student.__mro__)  # 查看类的继承关系

p = Persion()
print(p.xingshi)
print(p.getAddress())
