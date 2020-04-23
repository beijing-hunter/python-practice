class Student():
    fuse = "黄色"  # 类属性

    def __init__(self):
        self.name = "tom"

    @classmethod
    def getFuSe(cls):  # 类方法
        cls.name = "t"  # 类属性
        return cls.fuse

    @staticmethod
    def work():  # 静态方法
        return "吃饭"


print(Student.fuse)

print(Student.getFuSe())
print(Student.name)
print(Student.work())

stu = Student()
print(stu.name)
