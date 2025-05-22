# Day 81 | Decision Tree Hyperparameter Tunning | DT Overfitting & Underfitting



> Python
```python

class sklearn.tree.DecisionTreeClassifier(*, criterion='gini',
splitter='best', max_depth=None, min_samples_split=2,
min_samples_leaf=1, min_weight_fraction_leaf=0.0,
max_features=None, random_state=None, max_leaf_nodes=None,
min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0,
monotonic_cst=None)

```

## Most Usefull Parameter

> Criterion
```python

criterion: {“gini”, “entropy”, “log_loss”}, default=”gini”

```

The function to measure the quality of a split. Supported criteria are “gini” for the Gini impurity and “log_loss” and “entropy” both for the Shannon information gain, see Mathematical formulation.

##
> Splitter
```python

splitter: {“best”, “random”}, default=”best”

```
The strategy used to choose the split at each node. Supported strategies are “best” to choose the best split and “random” to choose the best random split.


##
> Max Depth 
```python

max_depth: int, default=None

```
The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.




##
> Min Samples Split
```python

min_samples_split: int or float, default=2

```
The minimum number of samples required to split an internal node:
- If int, then consider `min_samples_split` as the minimum number.
- If float, then `min_samples_split` is a fraction and `ceil(min_samples_split * n_samples)` are the minimum number of samples for each split



##
> Min Samples Leaf
```python

min_samples_leaf: int or float, default=1

```
The minimum number of samples required to be at a leaf node. A split point at any depth will only be considered if it leaves at least `min_samples_leaf` training samples in each of the left and right branches. This may have the effect of smoothing the model, especially in regression.

- If int, then consider `min_samples_leaf` as the minimum number.
- If float, then `min_samples_leaf` is a fraction and `ceil(min_samples_leaf * n_samples)` are the minimum number of samples for each node.




##
> Max Features
```python

max_features: int, float or {“sqrt”, “log2”}, default=None

```
The number of features to consider when looking for the best split:

- If int, then consider `max_features` features at each split.
- If float, then `max_features` is a fraction and `max(1, int (max_features * n_features_in_))` features are considered at - each split.
- If “sqrt”, then `max_features=sqrt(n_features)`.
- If “log2”, then `max_features=log2(n_features)`.
- If None, then `max_features=n_features`.




##
> Max Leaf Nodes
```python

max_leaf_nodes: int, default=None

```
Grow a tree with `max_leaf_nodes` in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.




##
> Min Impurity Decrease
```python

min_impurity_decrease: float, default=0.0

```
A node will be split if this split induces a decrease of the impurity greater than or equal to this value.

The weighted impurity decrease equation is the following:
N_t / N * (impurity - N_t_R / N_t * right_impurity
                    - N_t_L / N_t * left_impurity)


where N is the total number of samples, `N_t` is the number of samples at the current node, `N_t_L` is the number of samples in the left child, and `N_t_R` is the number of samples in the right child.

`N`, `N_t`, `N_t_R` and `N_t_L` all refer to the weighted sum, if `sample_weight` is passed.



## Overfitting & Underfitting
1. Criterion: Gini/Entropy
2. Splitter: Best/Random(`Reduced Overfitting`)
3. Max Depth: $0 - \infty$ (`Underfitting-Overfitting`)
4. Min Samples Split: $0 - \infty$ (`Overfitting-Underfitting`)
5. Min Samples Leaf: $0 - \infty$ (`Overfitting-Underfitting`)
6. Max Features:
7. Max Leaf Nodes: $0 - \infty$ (`Underfitting-Overfitting`)
8. Min Impurity Decrease: $0 - \infty$ (`Overfitting-Underfitting`)