def showMessage():
    return "hello world"


def addNum(v1, v2):
    """求v1，v2的和"""
    return v1 + v2


print(showMessage())
print(addNum(12, 23))
print(help(addNum))  # 查看函数说明文档
