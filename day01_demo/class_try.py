try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as result:  # 捕获指定类型的异常
    print(result)

try:
    print(1)
except Exception as result:  # 捕获所有异常
    print(result)
else:  # 没有异常发生时执行的代码
    print("我是else，没有异常发生时执行的代码")
finally:  # 无论是否发生异常都要执行的代码
    print("无论是否发生异常都要执行的代码")


class CustomException(Exception):
    def __init__(self, currentLength, minLength):
        self.currentLength = currentLength
        self.minLength = minLength

    def __str__(self):
        return f"您输入的密码长度{self.currentLength},密码长度不能少于{self.minLength}"


try:
    password = input("请输入密码:")
    if len(password) < 3:
        raise CustomException(len(password), 3)
except Exception as result:
    print(result)
else:
    print("密码输入完成")
