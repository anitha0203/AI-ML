## Supervised Learning 

**Supervised learning** is a category of machine learning in which an algorithm learns from labeled training data to make predictions or decisions without human intervention

-   Regression
    -   [Simple Linear Regression](#simple-linear-regression)
    -   [Multiple Linear Regression](#multiple-linear-regression)
    -   [Polynomial Regression](#polynomial-linear-regression)
    
-   Classification
    -   Logistic Regression
    -   Support vector Regression
    -   K-Nearest Neighbors
    -   Random Forest


### [Scaling](https://medium.com/analytics-vidhya/feature-scaling-clearly-explained-standardisation-normalization-6bc1a200a166)

**Standardization (Z-score scaling)**: This method scales data to have a mean of 0 and a standard deviation of 1. It's useful when the data approximately follows a normal distribution. The formula is:

**Implementing the Standardization for X and y**

        X = data.iloc[:, 0]
        y = data.iloc[:, 1]

        # Standardization for X
        mean_X = X.mean()
        std_X = X.std()
        X = (X - mean_X) / std_X

        # Standardization for y
        mean_y = y.mean()
        std_y = y.std()
        y = (y - mean_y) / std_y


## [Derivatives](https://www.youtube.com/watch?v=sqDBEyfRPo8)
Derivatives are a fundamental concept in calculus, and they play a crucial role in many machine-learning algorithms. Put simply, a derivative measures the rate of change of a function at a particular point. This information can be used to optimize functions, find local minima and maxima, and more.

    Note: Specifically using derivative to calculate the slope

## Simple Linear Regression 

Simple Linear Regression is a statistical method used to model the relationship between a single independent variable (predictor variable) and a dependent variable (target variable) by fitting a linear equation

**Note:** If you want to know more about SLR you can click below links watch it.
-   https://medium.com/we-are-orb/linear-regression-in-python-without-scikit-learn-50aef4b8d122
-   https://bagheri365.github.io/blog/Simple-Linear-Regression-from-Scratch/
-   https://medium.com/analytics-vidhya/everything-you-need-to-know-about-linear-regression-750a69a0ea50
-   https://medium.com/analytics-vidhya/understanding-the-linear-regression-808c1f6941c0
-   https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931

The Simple Linear Regression model can be represented by the equation:

Y = β0 + β1X + ε

Where:

-   Y is the predicted value of the dependent variable.
-   X is the value of the independent variable.
-   β0 is the intercept, representing the predicted value of Y when X is 0.
-   β1 is the slope, representing the change in Y for a one-unit change in X.
-   ε is the error term, representing the unexplained variation in Y.


## Multiple Linear Regression
Multiple Linear Regression is an extension of Simple Linear Regression and is a widely used statistical technique for modeling the relationship between a dependent variable (target) and two or more independent variables (predictors). 

The Multiple Linear Regression model can be represented by the equation:

Y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ... + βₚXₚ + ε

Where:

-   Y is the predicted value of the dependent variable.
-   X₁, X₂, X₃, ..., Xₚ are the values of the independent variables (predictors).
-   β₀ is the intercept, representing the predicted value of Y when all predictor variables are 0.
-   β₁, β₂, β₃, ..., βₚ are the coefficients (slopes) associated with each predictor variable, representing the change in Y for a one-unit change in the corresponding predictor variable.
-   ε is the error term, representing the unexplained variation in Y.

        w = np.zeros(X.shape[1])  # Weights
        b = 0  # Bias
        learning_rate = 0.01
        num_epochs = 1000

    This section initializes the parameters for a linear regression model. w represents the weights for the features, b is the bias term, learning_rate is the step size for gradient descent, and num_epochs is the number of training iterations.

##  Polynomial Regression

Polynomial Regression, often referred to as Polynomial Regression, is a regression technique that extends Simple Linear Regression. It is particularly useful when the relationship between variables does not follow a linear pattern but appears to be curvilinear.

Y = β₀ + β₁X + β₂X² + β₃X³ + ... + βₚXᵖ + ε

Where:

-   Y is the predicted value of the dependent variable.
-   X is the value of the independent variable.
-   β₀ is the intercept, representing the predicted value of Y when X is 0.
-   β₁, β₂, β₃, ..., βₚ are the coefficients (slopes) associated with each term of the polynomial, representing the change in Y for a change in the corresponding predictor(s).
-   ε is the error term, representing the unexplained variation in Y.