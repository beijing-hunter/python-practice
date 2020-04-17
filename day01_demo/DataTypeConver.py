num = input("请输入数字：")

print("您输入的数字是：%d" % int(num))

num1 = 10
strValue = "23"
listData = [12, 23, 132]

# float 转换
fNum = float(num1)
print("data type=%s,data value=%.2f" % (type(fNum), fNum))

# str 转换
strNum = str(num1)
print("data type=%s,data value=%s" % (type(strNum), strNum))

# str 转换
strList = str(listData)
print("data type=%s,data value=%s" % (type(strList), strList))

# tuple 转换
tupleData = tuple(listData)
print("data type=%s,data value=%s" % (type(tupleData), tupleData))

listDatas = list(tupleData)
print("data type=%s,data value=%s" % (type(listDatas), listDatas))

# eval() 计算在字符串中的有效python表达式，并返回一个对象，根据字符串中的值，自动转换为系统数据类型

str1 = "1"
str2 = "1.1"
str3 = "[12,12,34,34]"
str5 = "(34,23,12)"

str1Num = eval(str2)
print("data type=%s,data value=%s" % (type(str1Num), str1Num))
