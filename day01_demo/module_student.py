# 如果模块文件中有__all__列表，当使用from xxx import * 导入时，只能导入这个列表中的元素
__all__ = ["testA", "Student"]


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        return f"name={self.name},age={self.age}"


def testA():
    return "hello world"
