#!/usr/bin/env python
# coding=utf-8


import os
import sys
from PIL import Image, ImageDraw
import numpy as np
import cv2
# import dlib


def detect_object(infile, save_path):
    image = cv2.imread(infile)
    # '检测图片，获取人脸在图片中的坐标'
    size = image.shape[:2]  # 获得当前桢彩色图像的大小
    # image_set=np.zeros(size,dtype=np.float16)#定义一个与当前桢图像大小相同的的灰度图像矩阵
    image_grey = np.zeros(size, np.uint8)  # 创建一个空白图片
    #image_grey = Image.new(mode= 'RGBA',size = size, color = (117,255,0))
    #image_grey = cv2.imread(img_grey)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像
    # img_binary = cv2.threshold(image,127,255,0)#将灰度图片转化为二进制图片
    color = (135, 206, 250)  # 设置人脸框的颜色
    #eye_cascade = cv2.CascadeClassifier('/Users/liuqi/opencv/data/haarcascades/haarcascade_eye.xml')
    classfier = cv2.CascadeClassifier(
        '/Users/liuqi/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

    # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
    faceRects = classfier.detectMultiScale(
        grey, scaleFactor=1.3, minNeighbors=4, minSize=(32, 32))
    result = []

    im = Image.open(infile)
    if len(faceRects) > 0:  # 大于0则检测到人脸
        draw = ImageDraw.Draw(im)
        num = 0
        for faceRect in faceRects:
            num += 1
            # 单独框出每一张人脸
            x, y, w, h = faceRect
            # 画出矩形框
            #cv2.rectangle(image_grey, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
            cv2.rectangle(grey, (x - 10, y - 10),
                          (x + w + 10, y + h + 10), color, 2)
            a = im.crop(faceRect)
            file_name = os.path.join(save_path, str(num)+'.jpg')

        cv2.imwrite(file_name, grey)

        drow_save_path = os.path.join(save_path, 'out.jpg')
        im.save(drow_save_path, 'JPEG', quality=80)
    else:
        print('Error: cannot detect faces on %s' % infile)
    return 0

def process(infile):
    # 获取图片，进行检测
    #image = cv2.imread(infile)
    # ''在原图上框出头像并且截取每个头像到单独文件夹''
    # 创建输出图片的路径
    #im = Image.open(infile)
    path = os.path.abspath(infile)
    save_path = os.path.splitext(path)[0]+'_face'
    try:
        os.mkdir(save_path)
    except:
        pass

    faces = detect_object(infile, save_path)



process('2.jpg')
