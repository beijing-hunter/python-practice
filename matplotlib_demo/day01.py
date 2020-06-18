import matplotlib.pyplot as plt

# 创建画布
plt.figure(figsize=(20, 8), dpi=100)

x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 15, 13, 18, 16, 20, 10]
# 绘制图像（折线图）
plt.plot(x, y)

# 图像显示
plt.show()
