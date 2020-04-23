# 公共操作符+   字符串，列表、元组数据类型做合并操作
str1 = "hello"
str2 = " world"
print(str1 + str2)

list1 = [23, 13]
list2 = [35, 12]
print(list1 + list2)

# 公共操作符*  字符串，列表、元组数据类型做 复制 扩充变量中的数据
print(str1 * 5)
print(list1 * 6)

print(max(list1))
print(min(list1))

for item in range(1, 20, 2):
    print(item)
