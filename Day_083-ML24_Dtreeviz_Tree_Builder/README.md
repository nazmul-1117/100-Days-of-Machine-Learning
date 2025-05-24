# Day 89 | Awespme Tree Visulization | 

`dtreeviz` Library in Python
dtreeviz is a powerful Python library for visualizing decision trees in a more informative and visually appealing way than basic tree plots provided by libraries like scikit-learn. It generates rich, interpretable diagrams that show how decisions are made at each node, including feature values, class distributions, and prediction paths.

Unlike the default `plot_tree()` from `scikit-learn`, `dtreeviz `visualizations include:

- Detailed node splitting conditions
- Color-coded histograms or scatter plots at each node
- Support for both classification and regression trees
- Option to visualize decision paths for specific input samples


## Basic
>Terminal
```bash
!pip install dtreeviz             # install dtreeviz for sklearn
!pip install dtreeviz[xgboost]    # install XGBoost related dependency
!pip install dtreeviz[pyspark]    # install pyspark related dependency
!pip install dtreeviz[lightgbm]   # install LightGBM related dependency
!pip install dtreeviz[tensorflow_decision_forests]   # install tensorflow_decision_forests related dependency
!pip install dtreeviz[all] 

```

> Python
```python

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

import dtreeviz

iris = load_iris()
X = iris.data
y = iris.target

clf = DecisionTreeClassifier(max_depth=4)
clf.fit(X, y)

viz_model = dtreeviz.model(clf,
                           X_train=X, y_train=y,
                           feature_names=iris.feature_names,
                           target_name='iris',
                           class_names=iris.target_names)

v = viz_model.view()     # render as SVG into internal object 
v.show()                 # pop up window
v.save("/tmp/iris.svg")  # optionally save as svg

viz_model.view()       # in notebook, displays inline


```
