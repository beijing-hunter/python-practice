import numpy as np
import cv2

# 实例化代表图片的列表数据
img_list = [
    [[0, 0, 255], [0, 0, 255]],
    [[0, 255, 255], [0, 255, 255]],
    [[255, 0, 255], [255, 0, 255]],
]

# 把列表数据转换成numpy中的数组
img_array = np.array(img_list)

# 把转换好的数组对象写入到特定的文件中
cv2.imwrite("imges/demo3x2.png", img_array)
