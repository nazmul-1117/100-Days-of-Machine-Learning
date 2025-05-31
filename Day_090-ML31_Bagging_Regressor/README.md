# Day 090 | Bagging Ensemble | Bagging Regressor | Part 3

## Bagging Regressor: Short Documentation
**Definition:** An ensemble learning technique for regression that applies the **Bagging** (Bootstrap Aggregating) method to a base regression model. It trains multiple instances of the base regressor on different bootstrapped subsets of the training data and averages their predictions to produce a final prediction.

## Code
```python
class sklearn.ensemble.BaggingRegressor(
    estimator=None, n_estimators=10, *, max_samples=1.0, 
    max_features=1.0, bootstrap=True, bootstrap_features=False, 
    oob_score=False, warm_start=False, n_jobs=None, 
    random_state=None, verbose=0
)
```
---

## Mechanism:

1.  **Bootstrapping:** Create multiple random subsets of the training data by sampling with replacement.
2.  **Independent Training:** Train a base regression model (e.g., Decision Tree Regressor, Support Vector Regressor) on each of these bootstrapped subsets independently.
3.  **Averaging Predictions:** For a new data point, obtain the predictions from all the trained base regressors. The final prediction is the **average** of these individual predictions.

## Key Parameters (in scikit-learn's `BaggingRegressor`):

* `base_estimator`: The base regression model to be ensembled (e.g., `DecisionTreeRegressor()`).
* `n_estimators`: The number of base regressors to train.
* `max_samples`: The number of samples to draw from the original dataset (with replacement) to train each base estimator (can be an integer or a float between 0 and 1).
* `max_features`: The number of features to draw from the original dataset to train each base estimator (can be an integer or a float between 0 and 1).
* `bootstrap`: Whether samples are drawn with replacement (usually `True`).
* `bootstrap_features`: Whether features are drawn with replacement.

## Pros:
* Reduces variance and helps prevent overfitting in regression tasks.
* Improves the stability and robustness of the regression model.
* Can lead to better prediction accuracy compared to a single base regressor.
* Each base regressor is trained independently, allowing for parallel computation.
* Provides an Out-of-Bag (OOB) score for estimating generalization performance without a separate validation set.

## Cons:
* Can slightly increase bias.
* Reduces interpretability compared to a single base regressor.
* Might not significantly improve performance for already stable base regressors.

## Use When:

* You are using a regression model prone to high variance (e.g., complex Decision Tree Regressors).
* You want to improve the stability and prediction accuracy of your regression model.
* Computational resources allow for training multiple regressors.

## Example Base Regressors:

* `DecisionTreeRegressor`
* `KNeighborsRegressor`
* `SVR` (Support Vector Regressor)
* Even other ensemble methods (though less common).


## Images
![iamge1](assets/image.avif)