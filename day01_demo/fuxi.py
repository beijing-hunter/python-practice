
name="tom"
age=12
tz=12.3
print("我是：%s,今年：%d,体重：%.2f" % (name,age,tz))

valueStr=input("请输入值：")
value=eval(valueStr)

print("你输入的数据类型是：%s,值为：%s" % (type(value),value))