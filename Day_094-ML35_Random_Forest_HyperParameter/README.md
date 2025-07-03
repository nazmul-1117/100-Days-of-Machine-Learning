# Day 094 | Random Forest Hyperparameter

---
## Random Forest Hyperparameters

Tuning the hyperparameters of a **Random Forest** can significantly improve its performance. Below are the key hyperparameters you should know:

| **Hyperparameter**  | **Description**                                                      | **Common Values / Tips**                                    |
| ------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------- |
| `n_estimators`      | Number of trees in the forest                                        | More trees = better performance (but slower); e.g., 100–500 |
| `max_depth`         | Maximum depth of each tree                                           | Prevents overfitting; try values like 10, 20, None          |
| `min_samples_split` | Minimum samples required to split a node                             | Higher values reduce overfitting; default = 2               |
| `min_samples_leaf`  | Minimum samples required at a leaf node                              | Use 1–5 for small datasets; helps with smoothing            |
| `max_features`      | Number of features to consider when splitting                        | `'sqrt'` (classification), `'log2'`, or a float fraction    |
| `bootstrap`         | Whether to use bootstrap samples (True) or the whole dataset (False) | Default is `True`; set `False` for extra variance control   |
| `random_state`      | Seed for reproducibility                                             | Fix a value like 42 to make results consistent              |
| `n_jobs`            | Number of CPU cores used for training (parallel processing)          | `-1` to use all cores                                       |
| `oob_score`         | Whether to use Out-of-Bag samples to estimate accuracy               | Set `True` to enable OOB evaluation                         |
| `class_weight`      | Used for handling imbalanced datasets (classification only)          | `'balanced'`, `'balanced_subsample'`, or custom dict        |

## Example (scikit-learn):

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    max_features='sqrt',
    min_samples_split=4,
    min_samples_leaf=2,
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
```
