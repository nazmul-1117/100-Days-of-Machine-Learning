# Day 55 | Multiple Linear Regression | Costume Code Implement

## Costume Code Implement
> Python
```python
class MultipleRegressionClass:
    def __init__(self):
        self.coefficients = None
        self.intercept = None
    
    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)
        
        first_part = np.linalg.inv(np.dot(X.T, X))
        second_part = np.dot(X.T, y)
        betas = np.dot(first_part, second_part)
        
        self.intercept = betas[0]
        self.coefficients = betas[1:]
    
    def predict(self, X):
        return np.dot(X, self.coefficients)+self.intercept

```