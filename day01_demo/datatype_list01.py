datas = [12, 45, 14, 55]
datass=[]
print(''.join(datass))
print(datas[1])
print(datas.index(12))
print(datas.count(14))
print(len(datas))

if 12 in datas:
    print("存在12")
else:
    print("不存在12")

for item in datas:
    print(item, end=",")
print()

# append() 追加指定数据到列表末尾
datas.append(14)
print(datas)

# append() 追加的数据是一个序列，则追加整个序列到列表
datas.append([11, 19])
print(datas)

# extend() 列表结尾追加数据，如果数据是一个序列，则将整个序列的数据逐一添加到列表
datas.extend([33, 22])
print(datas)

# insert()
datas.insert(0, 90)
print(datas)

# del 删除列表
# del datas
# print(datas)

# del 指定下标数据
del datas[0]
print(datas)

"""
pop 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
pop函数返回整个被删除的数据
"""
valueItem = datas.pop(2)
print(valueItem)

# remove() 删除指定数据
datas.remove(33)  # 删除指定数据，如果数据不存在则报异常

# clear() 情况列表
# datas.clear()

for item in datas:
    datas.pop(0)
    print(datas)

# 逆序 reverse
datas.reverse()
print(datas)

# sort(key=None,revers=False) revers:排序规则，True降序，False升序（默认）；
# key:排序关键字，根据字典中的某个key排序
datas = [34, 12, 11, 0, 89]
datas.sort(reverse=True)
print(datas)

# copy 复制
newDatas = datas.copy()
newDatas[0] = -1
print(newDatas)
