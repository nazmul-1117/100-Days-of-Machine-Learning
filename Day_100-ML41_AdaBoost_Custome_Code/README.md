# Day 100 | AdaBoost Code | Customized Code | Code from Scratch

---

### ✅ Step-by-Step AdaBoost in Python

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

### Step 1: Create a Simple Dataset

```python
# Binary classification dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)

# Convert labels to -1 and +1
y = np.where(y == 0, -1, 1)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

### Step 2: Initialize Parameters

```python
# Number of weak learners
M = 10

# Initialize weights equally
N = len(X_train)
w = np.full(N, 1 / N)

# Store weak learners and their weights
learners = []
alphas = []
```

---

### Step 3: AdaBoost Iterations

```python
for m in range(M):
    # Train a weak learner with current weights
    stump = DecisionTreeClassifier(max_depth=1, random_state=42)
    stump.fit(X_train, y_train, sample_weight=w)
    y_pred = stump.predict(X_train)

    # Calculate weighted error
    err = np.sum(w * (y_pred != y_train)) / np.sum(w)

    # Compute alpha (learner weight)
    alpha = 0.5 * np.log((1 - err) / (err + 1e-10))  # add small term to avoid division by 0

    # Update sample weights
    w *= np.exp(-alpha * y_train * y_pred)
    w /= np.sum(w)  # normalize

    # Save learner and alpha
    learners.append(stump)
    alphas.append(alpha)

    print(f"Iteration {m+1}: Error={err:.4f}, Alpha={alpha:.4f}")
```

---

### Step 4: Make Final Predictions

```python
def adaboost_predict(X):
    final_pred = np.zeros(X.shape[0])
    for alpha, learner in zip(alphas, learners):
        final_pred += alpha * learner.predict(X)
    return np.sign(final_pred)
```

---

### Step 5: Evaluate

```python
y_pred_train = adaboost_predict(X_train)
y_pred_test = adaboost_predict(X_test)

print("Train Accuracy:", accuracy_score(y_train, y_pred_train))
print("Test Accuracy:", accuracy_score(y_test, y_pred_test))
```

---

### 🧠 Key Concepts Covered:

* Sample weighting
* Error and alpha calculation
* Updating weights for misclassified points
* Final weighted majority vote

---
