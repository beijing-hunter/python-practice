dictData = {"name": "tom", "age": 12, "tz": 12.3}

dicData01 = {}
print(type(dicData01))

dictData["name"] = "tom2"  # key存在，则为修改数据
dictData["id"] = "01"  # 不存在key,则为新增
print(dictData)
# print(dictData["stuNo"]) # key不存在，报出异常

# get() 方法
print(dictData.get("stuNo"))

keys = dictData.keys()
print(keys)
for keyItem in keys:
    print(keyItem)

values = dictData.values()
print(values)
for valueItem in values:
    print(valueItem)

itemDatas = dictData.items()
print(itemDatas)

for key, value in itemDatas:
    print(f"key={key},value={value}")

# 删除数据
del dictData["age"]
print(dictData)

dictData.clear()
print(dictData)
