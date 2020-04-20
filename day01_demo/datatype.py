num1 = 1
num2 = 1.1
# 获取数据类型 type()
print(type(num1))

strValue = "我用python"
print(type(strValue))

ab = True
print(type(ab))

# list
datas = [12, 1, 23]
print(type(datas))

# 元组
tdats = (12, 3, 2)
print(type(tdats))

# 定义元组是，单个元素后边，也要加上逗号，否则数据类型为单个元素的类型
tdatas01 = (12)  # 正确写法：tdatas01=(12,)
print(type(tdatas01))  # <class 'int'>

# set 集合
setDatas = {12, 14, 1}
print(type(setDatas))

# dict 字典
dictDatas = {"name": "tom", "age": 12}
print(type(dictDatas))
