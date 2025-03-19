# Day 65 | 5 key points for Ridge Regression
- **Regularization:** Ridge regression is a type of linear regression that adds a penalty term to the loss function. This penalty is the sum of the squared values of the coefficients multiplied by a constant factor (alpha or lambda).

- **Bias-Variance Trade-off:** Ridge regression helps to reduce model complexity and prevent overfitting by shrinking the coefficients towards zero. This introduces a small amount of bias but can significantly reduce variance, leading to improved generalization performance.

- **Multicollinearity:** Ridge regression effectively handles multicollinearity (high correlation between predictor variables) by stabilizing the coefficient estimates.

- **Hyperparameter Tuning:** The regularization parameter (alpha or lambda) controls the amount of shrinkage. It's crucial to tune this hyperparameter to find the optimal balance between bias and variance for your specific dataset.

- **Linear Model:** Ridge regression is still a linear model, meaning it assumes a linear relationship between the features and the target variable. It might not be suitable for highly non-linear data.