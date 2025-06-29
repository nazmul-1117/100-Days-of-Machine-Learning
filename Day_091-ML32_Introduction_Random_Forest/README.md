# Day 091 | Introduction Random Forest 

---

## Random Forest

**Random Forest** is a popular ensemble learning method based on **Bagging** that uses a collection of decision trees to make more accurate and robust predictions. It is used for both classification and regression tasks.

### How Random Forest Works:

1. **Bootstrap Sampling**: Like bagging, it creates multiple subsets of the training data using sampling with replacement.
2. **Random Feature Selection**: When building each decision tree, instead of considering all features at every split, it selects a **random subset of features**. This introduces more diversity among the trees.
3. **Aggregation**:

   * For **classification**, it uses majority voting.
   * For **regression**, it averages the outputs of all trees.

This extra randomness in feature selection reduces **correlation between trees**, making the ensemble even more powerful and less prone to overfitting than basic bagging.

### Example (using `scikit-learn`):

```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, max_features='sqrt')
rf_model.fit(X_train, y_train)
```

### Key Benefits:

* Handles large datasets and high-dimensional spaces well
* Reduces overfitting by averaging multiple trees
* Works well even without heavy parameter tuning
* Provides feature importance scores

Random Forest is widely used in real-world applications due to its **high accuracy**, **robustness**, and **interpretability**.

---


## Gemini
## Random Forest: Short Documentation

**Definition:** A powerful and versatile ensemble learning algorithm that operates by constructing a multitude of decision trees during training and outputting the mode of the classes (classification) or the mean prediction (regression) of the individual trees.

**Mechanism:**

1.  **Bootstrap Sampling:** Creates multiple subsets of the training data by sampling with replacement.
2.  **Random Feature Selection:** When building each tree, only a random subset of features is considered at each split.
3.  **Independent Tree Building:** Each decision tree is trained on a different bootstrap sample and with different random feature subsets.
4.  **Aggregation:**
    * **Classification:** The final class is determined by the majority vote among all trees.
    * **Regression:** The final prediction is the average of the predictions from all trees.

**Key Parameters (in scikit-learn's `RandomForestClassifier`/`RandomForestRegressor`):**

* `n_estimators`: The number of trees in the forest.
* `max_features`: The number of features to consider when looking for the best split at each node.
* `max_depth`: The maximum depth of each tree.
* `min_samples_split`: The minimum number of samples required to split an internal node.
* `min_samples_leaf`: The minimum number of samples required to be at a leaf node.
* `bootstrap`: Whether bootstrap samples are used when building trees (usually `True`).

**Pros:**

* High accuracy and robustness to outliers and noise.
* Effective for both classification and regression tasks.
* Can handle large datasets with high dimensionality.
* Provides estimates of feature importance.
* Reduces overfitting compared to single decision trees.
* Less sensitive to hyperparameter tuning than some other algorithms.

**Cons:**

* Can be computationally expensive for large numbers of trees.
* Less interpretable than single decision trees.
* May overfit noisy datasets.

**Use When:**

* You need a highly accurate and robust model.
* The dataset is large and has many features.
* Interpretability is not the primary concern.
* You want a good "out-of-the-box" algorithm that often performs well without extensive tuning.