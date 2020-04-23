# 集合中不可以有重复数据，如果有则自动去重,集合的存储是无序的,不支持用下标取值[index]
setDatas = {12, 12, 23, 45}
print(setDatas)  # 输入结果 12, 23, 45

setDatas01 = set("123444")
print(setDatas01)

setDatas02 = set()  # 创建空集合 只能用set(),

setDatas.add(30)
print(setDatas)

# update() 增加的数据是列表数据
setDatas.update([12, 34, 89, 23])
print(setDatas)

# 删除数据
setDatas.remove(12)  # 删除指定数据，如果数据不存在则报异常
print(setDatas)

setDatas.discard(12)  # 删除指定数据，如果数据不存在则不报异常

delValue=setDatas.pop()  # 随机删除一个数据
print(delValue)
print(setDatas)

# 判断数据是否存在

if 12 in setDatas:
    print("存在12")
else:
    print("不存在12")
