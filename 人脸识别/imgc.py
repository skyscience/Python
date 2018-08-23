import cv2 as cv

src=cv.imread('a1.jpg')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
 
#高度从42像素开始到282像素
#宽度从184像素开始到355像素
#高度起始位置是从图片的顶部算起，宽度起始位置是从图片的左侧算起
#本例中的起始位置和结束位置是通过PhotoShop 测量出来的，在实际应用中这两个位置是通过算法计算出来的
face=src[42:282,184:355]
#效果见图1，我们取出了原图的人脸
cv.imshow("取出的图像",face)
 
#将取出的区域改变为灰度图像
gray=cv.cvtColor(face,cv.COLOR_BGR2GRAY)
 
#将灰度图像变为RGB图像
#这里改变色彩空间的原因是灰度图像是单通道的，原图是三通道的，无法合并
#所以需要先转换为三通道的RGB色彩空间
backface=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
 
#将取出并处理完的图像和原图合并起来
src[42:282,184:355]=backface
#效果见图2
cv.imshow("合并后的图像",src)
 
 
cv.waitKey(0)
cv.destroyAllWindows() 