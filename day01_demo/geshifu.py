name = "tom"
age = 12
tiZho = 140.255
stuNo = 12
print('我是%s' % name)
print("年龄%d" % age)
print("体重%f" % tiZho)
print("体重%.2f" % tiZho)

# 整数值不足三位，前方补零
print("学号:%03d" % stuNo)

print("我是:%s,今年:%d,体重:%.2f,学号:%03d" % (name, age, tiZho, stuNo))

# f 格式语法 f{}
print(f"我是:{name},体重：{tiZho}")
