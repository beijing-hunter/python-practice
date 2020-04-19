b = 1
if b > 2:
    print(f"b大于2")

ageStr = input("请输入年龄：")
age = eval(ageStr)

if age >= 18:
    print(f"年龄{age},恭喜你成年了")
else:
    print(f"恭喜你还未成年，还可以浪{18-age}年")

# if多重判断
if age > 10 and age < 18:
    print("童工")
elif age >= 18 and age < 60:
    print("成年工人")
elif age >= 60 and age < 80:
    print("您可以退休了")
else:
    print("您已经超过人类平均年龄")

# if嵌套
a = age
if a >= 1:
    print(f"你有{a}元，可以进房间")
    cNumb = 12
    if cNumb > 12:
        print(f"还有{cNumb}床，你可以上床睡觉")
    else:
        print("有钱没床，站着睡吧")
else:
    print("没钱，走路")

# 三元运算符
d = "成年" if age >= 18 else "未成年"
print(d)

