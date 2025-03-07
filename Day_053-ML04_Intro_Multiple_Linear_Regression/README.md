# Day 53| Introduction to Multiple Linear Regression| 
Multiple linear regression extends simple linear regression to model the relationship between a dependent variable (y) and multiple independent variables (x₁, x₂, ..., xₚ). It aims to find the best linear relationship that predicts the dependent variable based on the combination of independent variables.

## The Model:
The multiple linear regression model is represented by the following equation: </br>
`y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε` </br>
Where:
- `y`: The dependent variable (response).
- `x₁, x₂, ..., xₚ`: The independent variables (predictors).
- `β₀`: The `y-intercept` (the value of y when all x variables are `0`).
- `β₁, β₂, ..., βₚ`: The `coefficients (slopes)` for each independent variable. They represent the change in y for a one-unit change in the corresponding x variable, holding all other x variables constant.
- `ε`: The error term (residual), representing the difference between the observed and predicted values of y.

## Code
> Python
```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
data = {'x1': [1, 2, 3, 4, 5],
        'x2': [2, 4, 5, 4, 5],
        'y': [3, 5, 7, 6, 9]}
df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df[['x1', 'x2']], df['y'], test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}")
print(f"R-squared: {r2}")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
```