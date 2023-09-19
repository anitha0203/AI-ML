# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)

# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x

# plt.scatter(x, y)
# plt.show()

# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]


# print(x)
# print(y)

# print(train_x)
# print(train_y)

# print(test_x)
# print(test_y)

# import matplotlib.pyplot as plt
# import numpy
# from sklearn import metrics

# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)

# confusion_matrix = metrics.confusion_matrix(actual, predicted)

# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

# cm_display.plot()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.show()