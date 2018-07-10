from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('./img/22.jpg')
# 获得图像尺寸:
w, h = im.size
print('图像尺寸 : %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('缩放后尺寸   : %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('./sc/thumbnail.jpg', 'jpeg')