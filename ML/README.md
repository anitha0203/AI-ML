#   Machine Learning

    Machine Learning is making the computer learn from studying data and statistics.
    Machine Learning is a step into the direction of artificial intelligence (AI).
    Machine Learning is a program that analyses data and learns to predict the outcome.

###  Data Types
To analyze data, it is important to know what type of data we are dealing with.

We can split the data types into three main categories:

-   Numerical
-   Categorical
-   Ordinal

**Numerical** data are numbers, and can be split into two numerical categories:
-   Discrete Data
    - numbers that are limited to integers. Example: The number of cars passing by.
-   Continuous Data
    - numbers that are of infinite value. Example: The price of an item, or the size of an item

**Categorical** data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.

**Ordinal** data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.


### Numpy
    import numpy as np
    speed = [86, 87, 82, 84, 84, 82]
    ages = [5,31,43,48,50,41,7,11,15,82,32,2,8,6,25,36,27,61,31]

    mean                = np.mean(speed)
    median              = np.median(speed)
    standardDeviation   = np.std(speed)
    variance            = np.var(speed)
    percentiles         = np.percentile(ages, 75) 
    
    
### Scipy
    import scipy as sp
    speed = [86, 87, 82, 84, 84, 82]

    mode                = sp.mode(speed)

### Histogram

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.random.uniform(0.0, 5.0, 250)

    plt.hist(x, 5)
    plt.show()

### Scatter Plot
A scatter plot is a diagram where each value in the data set is represented by a dot.

The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:

    import matplotlib.pyplot as plt

    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    plt.scatter(x, y)
    plt.show()

**Scatter Plot Explained**

The x-axis represents ages, and the y-axis represents speeds.

What we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.

### Regression
-   The term regression is used when you try to find the relationship between variables.

-   In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

### Linear Regression
Linear regression uses the relationship between the data-points to draw a straight line through all them.

This line can be used to predict future values.

    import matplotlib.pyplot as plt
    from scipy import stats

    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
    return slope * x + intercept

    mymodel = list(map(myfunc, x))

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()

### Polynomial Regression
If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

Polynomial regression, like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.

    import numpy
    import matplotlib.pyplot as plt

    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

    mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

    myline = numpy.linspace(1, 22, 100)

    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()

### Multiple Regression
Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.

### Scale Features

When your data has different values, and even different measurement units, it can be difficult to compare them. What is kilograms compared to meters? Or altitude compared to time?

The answer to this problem is scaling. We can scale data into new values that are easier to compare.

    import pandas
    from sklearn import linear_model
    from sklearn.preprocessing import StandardScaler
    scale = StandardScaler()

    df = pandas.read_csv("data.csv")

    X = df[['Weight', 'Volume']]

    scaledX = scale.fit_transform(X)

    print(scaledX)

### What is Train/Test

Train/Test is a method to measure the accuracy of your model.

It is called Train/Test because you split the data set into two sets: a training set and a testing set.

-   Train the model means create the model.
-   Test the model means test the accuracy of the model.


### Decision Tree
A Decision Tree is a Flow Chart, and can help you make decisions based on previous experience.

    import pandas
    from sklearn import tree
    from sklearn.tree import DecisionTreeClassifier

    df = pandas.read_csv("data.csv")

    d = {'UK': 0, 'USA': 1, 'N': 2}
    df['Nationality'] = df['Nationality'].map(d)
    d = {'YES': 1, 'NO': 0}
    df['Go'] = df['Go'].map(d)

    features = ['Age', 'Experience', 'Rank', 'Nationality']
    X = df[features]
    y = df['Go']

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, y)

    print(dtree.predict([[40, 10, 7, 1]]))

    print("[1] means 'GO'")
    print("[0] means 'NO'")
    
>   Different Results
>-   You will see that the Decision Tree gives you different results if you run it enough times, even if you feed it with the same data.
>-   That is because the Decision Tree does not give us a 100% certain answer. It is based on the probability of an outcome, and the answer will vary.

### What is a confusion matrix?
It is a table that is used in classification problems to assess where errors in the model were made.

The rows represent the actual classes the outcomes should have been. While the columns represent the predictions we have made. Using this table it is easy to see which predictions are wrong.

    import matplotlib.pyplot as plt
    import numpy
    from sklearn import metrics

    actual = numpy.random.binomial(1,.9,size = 1000)
    predicted = numpy.random.binomial(1,.9,size = 1000)

    confusion_matrix = metrics.confusion_matrix(actual, predicted)

    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

    cm_display.plot()
    plt.show()

### Hierarchical Clustering
Hierarchical clustering is an unsupervised learning method for clustering data points. The algorithm builds clusters by measuring the dissimilarities between data. Unsupervised learning means that a model does not have to be trained, and we do not need a "target" variable. This method can be used on any data to visualize and interpret the relationship between individual data points.

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.cluster.hierarchy import dendrogram, linkage

    x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

    data = list(zip(x, y))

    linkage_data = linkage(data, method='ward', metric='euclidean')
    dendrogram(linkage_data)

    plt.show()

### Logistic Regression
Logistic regression aims to solve classification problems. It does this by predicting categorical outcomes, unlike linear regression that predicts a continuous outcome.

In the simplest case there are two outcomes, which is called binomial, an example of which is predicting if a tumor is malignant or benign. Other cases have more than two outcomes to classify, in this case it is called multinomial. A common example for multinomial logistic regression would be predicting the class of an iris flower between 3 different species.

    import numpy
    from sklearn import linear_model

    #Reshaped for Logistic function.
    X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
    y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

    logr = linear_model.LogisticRegression()
    logr.fit(X,y)

    log_odds = logr.coef_
    odds = numpy.exp(log_odds)

    print(odds)

### Bagging
Methods such as Decision Trees, can be prone to overfitting on the training set which can lead to wrong predictions on new data.

Bootstrap Aggregation (bagging) is a ensembling method that attempts to resolve overfitting for classification or regression problems. Bagging aims to improve the accuracy and performance of machine learning algorithms. It does this by taking random subsets of an original dataset, with replacement, and fits either a classifier (for classification) or regressor (for regression) to each subset. The predictions for each subset are then aggregated through majority vote for classification or averaging for regression, increasing prediction accuracy.

### AUC - ROC Curve
In classification, there are many different evaluation metrics. The most popular is accuracy, which measures how often the model is correct. This is a great metric because it is easy to understand and getting the most correct guesses is often desired. There are some cases where you might consider using another evaluation metric.

Another common metric is AUC, area under the receiver operating characteristic (ROC) curve. The Reciever operating characteristic curve plots the true positive (TP) rate versus the false positive (FP) rate at different classification thresholds. The thresholds are different probability cutoffs that separate the two classes in binary classification. It uses probability to tell us how well a model separates the classes.

### KNN (K-Nearest Neighbors Algorithm)
KNN is a simple, supervised machine learning (ML) algorithm that can be used for classification or regression tasks - and is also frequently used in missing value imputation. It is based on the idea that the observations closest to a given data point are the most "similar" observations in a data set, and we can therefore classify unforeseen points based on the values of the closest existing points. By choosing K, the user can select the number of nearby observations to use in the algorithm.

Here, we will show you how to implement the KNN algorithm for classification, and show how different values of K affect the results.