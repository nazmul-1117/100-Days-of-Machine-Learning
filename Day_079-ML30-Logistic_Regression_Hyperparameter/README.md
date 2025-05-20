# Day 79 | Logistic Regression Hyperparameter Tunning
Some Famous Hyperparameter Tunning

> Python
```python
class sklearn.linear_model.LogisticRegression(penalty='l2', *,
dual=False, tol=0.0001, C=1.0, fit_intercept=True,
intercept_scaling=1, class_weight=None, random_state=None,
solver='lbfgs', max_iter=100, multi_class='deprecated',
verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
```

## Parameter
> penalty
```python
penalty{‘l1’, ‘l2’, ‘elasticnet’, None}, default=’l2’
```
- Specify the norm of the penalty:
  - `None:` no penalty is added;
  - `'l2'`: add a L2 penalty term and it is the default choice
  - `'l1'`: add a L1 penalty term;
  - `'elasticnet'`: both L1 and L2 penalty terms are added.


> Tolerance
```python
tol: float, default=1e-4
```

> C {inverse Lambda}
```python
C : float, default=1.0
```
Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.


> Class Weight (Imbalance Datasets)
```python
class_weight : dict or ‘balanced’, default=None
```
class_weightdict or ‘balanced’, default=None
Weights associated with classes in the form {class_label: weight}. If not given, all classes are supposed to have weight one.

The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as n_samples / (n_classes * np.bincount(y)).

Note that these weights will be multiplied with sample_weight (passed through the fit method) if sample_weight is specified.


> Solver
```python
solver : {‘lbfgs’, ‘liblinear’, ‘newton-cg’, ‘newton-cholesky’, ‘sag’, ‘saga’}, default=’lbfgs’
```

Algorithm to use in the optimization problem. Default is ‘lbfgs’. To choose a solver, you might want to consider the following aspects:

- For small datasets, ‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones;

- For multiclass problems, all solvers except ‘liblinear’ minimize the full multinomial loss;

- ‘liblinear’ can only handle binary classification by default. To apply a one-versus-rest scheme for the multiclass setting one can wrap it with the OneVsRestClassifier.

- ‘newton-cholesky’ is a good choice for `n_samples >> n_features * n_classes`, especially with one-hot encoded categorical features with rare categories. Be aware that the memory usage of this solver has a quadratic dependency on `n_features * n_classes` because it explicitly computes the full Hessian matrix.

> Epochs
```python
max_iter : int, default=100
```
Maximum number of iterations taken for the solvers to converge.

> Multi Class
```python
multi_class : {‘auto’, ‘ovr’, ‘multinomial’}, default=’auto’
```
- If the option chosen is ‘ovr’, then a binary problem is fit for each label. For ‘multinomial’ the loss minimised is the multinomial loss fit across the entire probability distribution, even when the data is binary. ‘multinomial’ is unavailable when solver=’liblinear’. ‘auto’ selects ‘ovr’ if the data is binary, or if solver=’liblinear’, and otherwise selects ‘multinomial’.

## Images
![source](assets\Capture.JPG)
![source](assets\Capture1.JPG)