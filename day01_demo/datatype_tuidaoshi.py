# list 推导式
list1 = [i for i in range(2, 10, 2)]
print(list1)

list2 = [i for i in range(100) if i % 2 == 0]
print(list2)

# dict 推导式
dic1 = {i: i * 2 for i in range(10)}
print(dic1)

list3 = ["name", "age", "tz", "no"]
list4 = ["tome", "12", "23.4"]
dic2 = {list3[i]: list4[i] for i in range(len(list4))}
print(dic2)

dic3 = {"LX": 120, "SX": 100, "HP": 200, "HW": 50, "HS": 250}
dic4 = {key: value for key, value in dic3.items() if value >= 120}
print(dic4)

# set 推导式
set1 = {i for i in dic3.keys()}
print(set1)
