# Day 097 | Feature Importance | Decision Tree and Random Forest

---

## Feature Importance

**Feature Importance** refers to techniques that assign a score to input features based on how useful they are at predicting the target variable. It helps identify **which features contribute most** to the model's decision-making process.

### In Decision Trees & Random Forests:

In tree-based models like **Random Forests**, feature importance is typically calculated based on how much each feature **reduces impurity** (e.g., Gini or Entropy) across all trees.

### How It Works (Intuition):

* Every time a feature is used to split a node, the **impurity decreases**.
* The more a feature contributes to impurity reduction across the forest, the **more important** it is.
* The importance values are then **normalized** so they sum to 1.

### Calculations
#### Formula:
- $X_i = \displaystyle \frac{N_t}{N} [impurity - (\frac{N_{tr}}{N_t} X Right_{impurity})- (\frac{N_{tl}}{N_t} X Left_{impurity})]$

- $\displaystyle f_i = \frac{\sum X_i}{\sum X+Y}$


Where,
- $N_t =$ on that's node total row number
- $N =$ Total Row Number
- $impurity =$ Gini/Entropy Number
- $N_{tr}=$ Right Node Row Number (Sample Number)
- $N_{tl}=$ Left Node Row Number (Sample Number)
- $Right_{impurity}=$ Right Impurity (Gini Number)
- $Left_{impurity}=$ Left Impurity (Gini Number)
- $\sum X_i=$ Total $X[0] or X[1]$
- $\sum X+Y=$ Total $X[0] + X[1]$

> Note: For More Details, See the `Notebook`


### Example (scikit-learn):

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Train model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Get feature importances
importances = rf.feature_importances_
feature_names = X_train.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
print(importance_df.sort_values(by='Importance', ascending=False))
```

#### Visualization:

```python
import matplotlib.pyplot as plt

# Plot feature importance
plt.barh(feature_names, importances)
plt.xlabel("Feature Importance")
plt.title("Random Forest Feature Importance")
plt.show()
```

### Why It’s Useful:

* Helps in **feature selection** (drop less important features)
* Improves **model interpretability**
* Guides **domain understanding** (e.g., which medical factors are most predictive)

### Limitations:

* Can be **biased** toward features with more categories or higher cardinality
* Doesn’t capture **feature interactions** well

---