import cv2
import dlib

# 读取图片
imgfile = cv2.imread("imges/demo3x2.png")
# 打印图片像素内容
print(imgfile)
# 查看维度信息
print(imgfile.shape)  # (3, 2, 3) 表示：三维数组，两个像素点、三通道
