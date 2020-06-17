# 彩色图片（rgb）转换为灰度图片
import cv2

# 读取彩色图片
rgb_img_file = cv2.imread("imges/Z0128.jpg")
# 彩色图片转换为灰度图片
gray_img_file = cv2.cvtColor(rgb_img_file, cv2.COLOR_BGR2GRAY)
# 查看灰度图片的像素信息
print(gray_img_file)
# 查看灰度图片的维度信息
print(gray_img_file.shape)
# 保存灰度图片
cv2.imwrite("imges/Z0128_gray.jpg", gray_img_file)

"""
灰度图的作用：计算机中的灰度图像是用二维数组表示的，灰度图像起到了降维的作用，方便计算机快速处理
"""
