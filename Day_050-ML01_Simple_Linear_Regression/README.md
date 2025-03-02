# Day_050 | Machine Learning Algorithm 001 | Simple Linear Regression

Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable. `y = mx+c`

## What is the best Fit Line?
The best Fit Line equation provides a straight line that represents the relationship between the dependent and independent variables. The slope of the line indicates how much the dependent variable changes for a unit change in the independent variable(s).

## 1. Simple Linear Regression

Simple linear regression is the simplest form of linear regression and it involves only one independent variable and one dependent variable. The equation for simple linear regression is: `y = mx + c`

where:
- `Y` is the dependent variable
- `X` is the independent variable
- `c` is the intercept
- `m` is the slope

## KeyWord:
1. Simple Linear Regression
2. Sort of Linear
3. Best fit line

> LinearRegression Apply | Python
```python
lr = LinearRegression()
lr.fit(X_train, y_train)
```

> Predict Test Data | Python
```python
lr.predict(X_test.iloc[0].values.reshape(1, 1))
```

> Draw Plot with Best fit line
```python
plt.scatter(df['cgpa'],df['package'])
plt.plot(X_train,lr.predict(X_train),color='red')
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')
```

> Find `m`
```python
m = lr.coef_
m
```

> Find `c`
```python
c = lr.intercept_
c
```