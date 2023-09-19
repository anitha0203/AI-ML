##  Machine Learning

**Artificial Intelligence** -   Engineering of making machines and programs

**Machine** - Enables machines to learn without being explicitly programmed


>Data science and machine learning go hand in hand. Data science helps evaluate data for machine learning algorithms.

-   Data science is the use of statistical methods to find patterns in the data.
-   Statistical machine learning uses the same techniques as data science.
-   Data Science includes techniques like statistical modeling, visualizatiom, and pattern recognition.
-   Machine Learning focuses on developing algorithms from the data provided.


The capability of artificial intelligence systems to learn by extracting patterns from data is known as **machine learning**.

**Features of Machine Learning**
-   It uses the data to detect patterns in a dataset and adjust program actions accordingly
-   It focuses on the development of computer programs that can teach themselves to grow and change when exposed to new data
-   It enables computers to find hidden insights using iterative algorithms without being explicitly programmed
-   It automates analytical model building using statistical and machine learning algrithms

### Supervised Learning
Supervised Learning is a type of machine learning used to train models from labeled training data. It allows you to predict the output for futre or unseen data.

**Types of Supervised Learning**
-   Classification
    -   The output has predefined labels that have discrete values.
    -   The goal is to predict discrete values that belong to a particular class and evaluate on the basis of accuracy.

-   Regression
    -   The output has a continuous value that is not restricted to defined separate values.
    -   Regression predicts a value as close to the actual output value as possible and evaluates it by calculating error value.
    -   The error value is inversely proportional to accuracy of model.



### Decision Tree Formation
Decision tree formation depends on two things:

Entropy:

-   Measures the impurity of a collection of examples.
-   Depends on the distribution of the random variable.
-   Measures the amount of information in a random variable.
    Formula: H(X) = -Σ P(ci) log2(Pi) = Σ (ei - 1) log2(1/Pi).
    X = {i, ..., C} for classification in C classes.

Information Gain:

-   Expected reduction in entropy caused by partitioning the examples on an attribute.
-   Higher the information gain, the more effective the attribute in classifying training data.
    Formula: Gain(S, A) = Entropy(S) - Σ (|Sv| / |S|) * Entropy (Sv) (where Sv represents subsets after partitioning).
    Values(A): possible values for attribute A.
                                                           |


### Unsupervised Learning
It is a technique used to train the machine learning algorithms using data that is either unclassified or unlabeled, which allows an algorithm to act on this data without guidence.