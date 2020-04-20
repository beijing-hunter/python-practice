strValue = "hello world"

# 下标取值
print(f"根据下标取字符：{strValue[0]}")

# 切片取值
print(strValue[2:7:1])
print(strValue[2:7])
print(strValue[:7])
print(strValue[2:])
print(strValue[:])
print(strValue[::2])  # 步长为2

print(strValue[::-1])  # 取所有值，倒序排序

# 常用方法

print(strValue.count("l"))  # 字符出现的次数
print(strValue.find("w"))  # 返回字符下标位置，没有返回-1
# print(strValue.index("i"))  # 返回字符下标位置，没有报出异常

newStr = strValue.replace("l", " and ")
print(newStr)

strValues = strValue.split("l")
print("strValues type=%s,datas=%s" % (type(strValues), strValues))

# join() 合并列表里面的 字符串 数据为一个大字符串
myStr = ["12", "34", "16", "14"]
newStr = "...".join(myStr)
print(newStr)

print(strValue.upper())  # 小写转换大写
print(strValue.lower())  # 大写转小写

print("  hello world  ".strip())  # 删除字符串两则空格符

print(strValue.startswith("h"))
print(strValue.endswith("h"))

# isalpha() 字符串都是字母返回true
print(strValue.isalpha())
print("hello".isalpha())

# isdigit() 字符串都是数字返回true
print("13244".isdigit())

# isalnum() 字符串都是数字或字母或组合返回true
print("ssss12223".isalnum())
print("ssss".isalnum())
print("21352111".isalnum())

# isspace() 都是空格，返回true
print("  s  ".isspace())
print("    ".isspace())

