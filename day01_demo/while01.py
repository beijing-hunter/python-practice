count = 1
while count <= 12:
    print(f"第{count}天，上课")
    count += 1

count = 1
total = 0
while count <= 100:
    if (count % 2) == 0:
        total += count
    count += 1
print(f"偶数之和{total}")

count = 1
while count <= 5:
    print(f"吃了{count}馒头")
    if count == 3:
        print("吃饱了")
        break
    count += 1

while count >= 3 and count<=12:
    print("while")
    count+=1
else:
    print("else exit")

abc = "21dsewf"
for item in abc:
    print(item)
