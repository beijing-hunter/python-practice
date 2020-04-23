def showMessage():
    return "hello world"


def addNum(v1, v2):
    """求v1，v2的和"""
    return v1 + v2


a = 150


def testB():
    a = 200
    print(f"testB value{a}")


def testA():
    print(f"testA value{a}")


print(testB())
print(testA())

print(showMessage())
print(addNum(12, 23))
print(help(addNum))  # 查看函数说明文档


def addAndSub(v1, v2):
    """求和及求差"""
    return v1 + v2, v1 - v2  # 返回的是元组数据类型


sumNum, subNum = addAndSub(12, 3)  # 拆包
print(sumNum, subNum)

values = addAndSub(v2=12, v1=3)
print(values)


# 不定长参数 定义（元组数据类型）
def userInfo(*params):
    print(params)


print(userInfo(12, 24, 23, 234))


# 不定长参数 定义（字典数据类型）
def userInfos(**params):
    print(params)


print(userInfos(name="tom", age=12, tz=13.4))

str1 = "hello"
print(id(str1))
str1 = str1 + " world"
print(id(str1))

fn1 = lambda a: a if a > 0 else -a

def addNum1(v1, v2, func):
    return func(v1) + func(v2)

print(addNum1(-12, -23, fn1))  # lambda 函数
print(addNum1(-12, -23, abs))  # 内置的绝对值函数abs()
