# Day 101 | AdaBoost Hyperparameters

---

## 🔧 AdaBoost Hyperparameters

When using `AdaBoostClassifier` in `scikit-learn`, you can control its behavior and performance through various **hyperparameters**. Tuning these properly can significantly affect your model’s accuracy and robustness.

---

## 🛠️ Key Hyperparameters

| Parameter                                               | Description                                                                                                                      |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **`n_estimators`**                                      | Number of weak learners (default = 50). More estimators can improve performance but may increase overfitting.                    |
| **`learning_rate`**                                     | Shrinks the contribution of each weak learner. Lower values make learning slower but more robust (default = 1.0).                |
| **`base_estimator`** (or `estimator` in newer versions) | The weak learner to use. Default is a decision stump (`DecisionTreeClassifier(max_depth=1)`). You can try other classifiers too. |
| **`algorithm`**                                         | `'SAMME'` or `'SAMME.R'`. `'SAMME.R'` uses class probabilities and is usually better for performance. Default is `'SAMME.R'`.    |
| **`random_state`**                                      | For reproducibility.                                                                                                             |

---

## 🧪 Example: Customizing AdaBoost

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

model = AdaBoostClassifier(
    base_estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=100,
    learning_rate=0.5,
    algorithm='SAMME.R',
    random_state=42
)
```
[AdaBoost-Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
---

## ✅ Tips for Hyperparameter Tuning

* **Start with default settings**, then tune `n_estimators` and `learning_rate`.
* Use **GridSearchCV** or **RandomizedSearchCV** to find the best combo.
* **Lower learning rate + more estimators** often gives better results but takes longer.

---


