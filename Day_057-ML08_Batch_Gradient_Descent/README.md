# Day  057 | Batch Gradient Descent | Multiple LinearRegression with Gradient Descent
Batch gradient descent (BGD) is a machine learning algorithm that updates model parameters using the entire training dataset. It's also known as vanilla gradient descent. 

## How it works
- BGD calculates the error for each example in the training dataset 
- It calculates the average gradient of the cost function for all the training examples 
- It updates the model's parameters in the opposite direction of the gradient 

## Advantages 
- BGD is computationally efficient
- It produces a stable error gradient and a stable convergence
- It's good at converging to the optimal solution

## Disadvantages 
- It can be slow for large datasets
- The stable error gradient can sometimes result in a suboptimal convergence
- It requires the entire training dataset to be in memory

## Related gradient descent algorithms 
- **Stochastic gradient descent:** Uses a single observation to calculate the cost
- **Mini-batch gradient descent:** Uses a subset of the entire dataset to calculate the cost

## Mathematics Calculation
assume a `2x3` dataframe with `(2, 2)` features and `(2, 1)` label. Columns are `cgpa(x1)`, `iq(x2)`, and `lpa(y)`
- if (n x m) matrix (2, 2)
- Coefficiant will be `(n+1)` which is `3` in this case

**Loss Function:** y = $\beta_0$ + $\beta_1 X_1$ + $\beta_2 X_2$
- $X_1$ is column 1 `CGPA`
- $X_2$ is column 2 `IQ`


Here, for this function `loss function's` parameter is L($\beta_0$, $\beta_1$, $\beta_2$). 
We have to find actual value of these  L($\beta_0$, $\beta_1$, $\beta_2$)

### Some Steps for calculate these ($\beta_0$, $\beta_1$, $\beta_2$)

1. Step: Assume
      1. $\beta_0$ = 0 (intercept)
      2. $\beta_1 \beta_2$ = 1 (coefficient)
2. Step: assume
   1. epochs=100
   2. learning_rate = 0.01
      1. $\beta_0$ = $\beta_0$ - $\eta *slop_1$
      2. $\beta_1$ = $\beta_1$ - $\eta *slop_2$
      3. $\beta_2$ = $\beta_2$ - $\eta *slop_3$
      3. $\beta_n$ = $\beta_n$ - $\eta *slop_n$
   3. Here, $slop_n$ is partial derivatives with respect to $\beta_n$ (`dL/dBn`)
3. Calculate the slop:

### Calculate the slop function
- Loss Function L = ($\beta_0$, $\beta_1$, $\beta_2$)
- Loss Function L = $\frac{1}{n}$ $\sum_{i=1}^{n} (y_i-\hat{y_i})^2$
- L = $\frac{1}{n}$ $[(y_1-\hat{y_1})^2 + (y_2-\hat{y_2})^2]$ [Here i have only two rows]
- L = $\frac{1}{n}$ $[(y_1 - (\beta_0 + \beta_1 X_11 + \beta_2 X_12))^2 + (y_2-(\beta_0 + \beta_1 X_21 + \beta_2 X_22))^2]$

This is the main equation for loss function. if we have `m` rows and `n` columns then we have the equation
- L = $\frac{1}{n}$ $[(y_1 - (\beta_0 + \beta_1 X_11 + \beta_2 X_12))^2 + (y_2-(\beta_0 + \beta_1 X_21 + \beta_2 X_22))^2 + (y_m-(\beta_0 + \beta_1 X_m1 + \beta_2 X_m2 + ...  + \beta_n X_mn))^2]$

### Derivatives this equation with respect to $\beta_0$, `m` is rows number
- $\frac {δL}{δ\beta_0}$ = $\frac{1}{m}$ $[2*(y_1-\hat{y_1})(-1) + 2(y_2-\hat{y_2})(-1)]$
- $\frac {δL}{δ\beta_0}$ = $-\frac{2}{m}$ $[(y_1-\hat{y_1})+ (y_2-\hat{y_2})]$
- $\frac {δL}{δ\beta_0}$ = $-\frac{2}{m}$ $[(y_1-\hat{y_1})+ (y_2-\hat{y_2}) + ... + (y_m-\hat{y_m})]$
- $\frac {δL}{δ\beta_0}$ = $-\frac{2}{m}$ $\sum(y_i-\hat{y_i})$

So, <span style="color:yellow;">**$\beta_0$ = $-\frac{2}{m}$ $\sum(y_i-\hat{y_i})$**</span>

### Derivatives this equation with respect to $\beta_1$, `m` is rows number
- $\frac {δL}{δ\beta_1}$ = $\frac{1}{m}$ $[2*(y_1-\hat{y_1})(-x_11) + 2(y_2-\hat{y_2})(-x_21)]$
- $\frac {δL}{δ\beta_0}$ = $-\frac{2}{m}$ $[(y_1-\hat{y_1})(x_11)+ (y_2-\hat{y_2})(x_21)]$
- $\frac {δL}{δ\beta_0}$ = $-\frac{2}{m}$ $\sum(y_i-\hat{y_i}) *$ X<sub>i1<sub>

So, <span style="color:	#ff00ff;">**$\beta_1$ = $-\frac{2}{m}$ $\sum(y_i-\hat{y_i})$ X<sub>i1<sub>**</span>

### Derivatives this equation with respect to $\beta_2$, `m` is rows number
<span style="color: #01cce9;">**$\beta_2$ = $-\frac{2}{m}$ $\sum(y_i-\hat{y_i})$ X<sub>i2<sub>**</span>

### General form for `n` columns and `m` rows
<span style="color: #01cce9;">**$\beta_m$ = $-\frac{2}{m}$ $\sum(y_i-\hat{y_i})$ X<sub>in<sub>**</span>
- Here
  - `i`  is rows index
  - `n` is columns index

## Implementation Derived in Python
- $\frac{1}{n} \sum$ = mean
- $(y_i - \hat{y_i})$
  - $y_i$ = Output Columns 
  - $\hat{y_i}$ = Output Prediction Column

Calculate $\hat{y_i}$
- $\hat{y_1}$ = $\beta_0$ + $\beta_1X_11$ + $\beta_2X_12$ + $\beta_3X_13$
- $\hat{y_2}$ = $\beta_0$ + $\beta_1X_21$ + $\beta_2X_22$ + $\beta_3X_23$
- $\hat{y}$ = $\beta_0$ + $\begin{bmatrix}X11 &X12 &X13\\X21 & X22 & X23 \end{bmatrix}$ $\begin{bmatrix} \beta_1 \\\ \beta_2 \\ \beta_2 \end{bmatrix}$
- np.dot(X_train, coefficient) + $\beta_0$
- Calculate $X_im$ = X_train


## Code Implement in python
>Python

```python
class CustomeGD:
    def __init__(self, learning_rate=0.01, epochs=100):
        self.coef_ = None
        self.intercept_ = None
        self.lr = learning_rate
        self.epochs = epochs

    def fit(self, X_train, y_train):
        self.intercept_ = 0
        self.coef_ = np.ones(X_train.shape[1])

        for i in range(self.epochs):

            # find the intercept (c)
            y_hat = np.dot(X_train, self.coef_) + self.intercept_
            intercept_der = -2 * np.mean(y_train - y_hat)
            self.intercept_ = self.intercept_ - (self.lr * intercept_der)

            # find the coef
            coef_der = -2 * np.dot((y_train - y_hat), X_train)/X_train.shape[0]
            self.coef_ = self.coef_ - (self.lr * coef_der)

    def predict(self, X_test):
        return np.dot(X_test, self.coef_) + self.intercept_
```




