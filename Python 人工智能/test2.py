import matplotlib.pyplot as plt

# 导入数据，分类器与性能度量
from sklearn import datasets, svm, metrics, linear_model

# # ================获取数据================
digits = datasets.load_digits()

# 这里使用的样本是8*8的图片,
# 先来看前4张图片，图片可以通过digits.images访问.
# 注意每张图片的尺寸必须相同以便使用W进行训练.
# 通过digits.target获取这张图片的标注。
images_and_labels = list(zip(digits.images, digits.target))

for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index+1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r)
    plt.title('Training: {}'.format(label))

# 要在样本图片上应用分类器，需要先将图片展开成shape为（样本数量，特征数量）的矩阵。
# ================预处理================
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# 创建分类器（获取模型）
classifier = linear_model.LogisticRegression()

# ================训练（+评估）================
# 取前一半的样本进行训练
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# ================测试================
# 对后一半的样本进行预测（测试）:
expected = digits.target[n_samples // 2:]

# 使用训练好的分类器（模型）进行预测
predicted = classifier.predict(data[n_samples // 2:])

# 计算准确率
print(metrics.accuracy_score(expected, predicted))

# 可视化测试结果
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index+5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r)
    plt.title('Prediction: {}'.format(prediction))

plt.show()