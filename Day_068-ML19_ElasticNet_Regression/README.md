# Day 68 | ElasticNet Regression
Elastic Net Regression is a regularized regression method that combines the `L1 (Lasso)` and `L2 (Ridge)` penalties to address multicollinearity and perform feature selection, offering a balance between coefficient shrinkage and sparsity. 

## Key Concepts:
1. Regularization:
Elastic Net, like Lasso and Ridge regression, aims to prevent overfitting by adding a penalty term to the loss function, shrinking coefficients and potentially setting some to zero. 

### L1 (Lasso) Penalty:
Encourages sparsity by shrinking coefficients towards zero, effectively performing feature selection. 

### L2 (Ridge) Penalty:
Shrinks coefficients towards zero, but less aggressively than L1, helping to address multicollinearity. 

### Combining L1 and L2:
Elastic Net combines both L1 and L2 penalties, allowing for a balance between feature selection and coefficient shrinkage, making it suitable for datasets with correlated features. 

### Tuning Parameters:
Elastic Net has two main tuning parameters:
- `λ (lambda)`: Controls the overall regularization strength. 
- `α (alpha)`: Determines the relative weight of the L1 and L2 penalties (α=1 is Lasso, α=0 is Ridge). 

## Advantages:
- **Handles Multicollinearity:** Elastic Net can effectively handle datasets with correlated features, unlike Lasso which might randomly select one from a group of correlated features. 
- **Feature Selection:** It can perform feature selection by shrinking coefficients of less important features to zero. 
- **Flexibility:** The combination of L1 and L2 penalties provides flexibility in handling different types of data and problems. 

## When to use Elastic Net:
- When you have a dataset with a large number of features and some of them are highly correlated. 
- When you want to perform feature selection and address multicollinearity simultaneously. 

## Mathematical Formula
- Loss Function L = $\sum_{i=1}^{n} (y_i-\hat{y_i})^2 +  a||\omega||^2 + b||\omega||$
- $\lambda = a+b$
- l1 _ratio = $\frac{a}{a+b} = \frac{a}{\lambda}$

## Implementation
>Python ElasticNet
```python
reg4 = ElasticNet(alpha=0.005, l1_ratio=0.95)
reg4.fit(X_train, y_train)
r2_score(y_test, reg4.predict(X_test))
```

>Python SGDRegressor
```python
reg5 = SGDRegressor(penalty='elasticnet', l1_ratio=0.95, alpha=0.005, max_iter=100000)
reg5.fit(X_train, y_train)
r2_score(y_test, reg5.predict(X_test))
```