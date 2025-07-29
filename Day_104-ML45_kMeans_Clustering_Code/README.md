# Day 104 | k-Means Clustering | Scikit Learn Code 

---

### 📦 `sklearn.cluster.KMeans`

The `KMeans` class in `scikit-learn` is used to perform **K-Means clustering**, an **unsupervised** algorithm that partitions data into `n_clusters` based on similarity.

---

### ✅ Class Syntax

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=8,
    init='k-means++',
    n_init='auto',
    max_iter=300,
    tol=1e-4,
    verbose=0,
    random_state=None,
    copy_x=True,
    algorithm='lloyd'
)
```

---

### 🧠 Important Parameters

| Parameter          | Description                                                                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`n_clusters`**   | Number of clusters to form. Must be an integer ≥ 1.                                                                                                                          |
| **`init`**         | Initialization method for centroids. `'k-means++'` (default) is efficient and helps avoid poor clustering. Other options: `'random'`, or pass an array of initial centroids. |
| **`n_init`**       | Number of times the algorithm runs with different centroid seeds. `'auto'` chooses the best default; usually 10 for `'k-means++'`.                                           |
| **`max_iter`**     | Maximum number of iterations per run of the algorithm. Default = 300.                                                                                                        |
| **`tol`**          | Tolerance for convergence. Small values mean more precise results but longer training time.                                                                                  |
| **`verbose`**      | Set to >0 to print detailed logs during fitting.                                                                                                                             |
| **`random_state`** | Controls randomness for reproducibility.                                                                                                                                     |
| **`copy_x`**       | If False, may overwrite input data for efficiency.                                                                                                                           |
| **`algorithm`**    | Algorithm for clustering. Options: `'lloyd'` (standard), `'elkan'` (faster for dense small datasets with fewer clusters).                                                    |

---

### ⚙️ Methods

| Method             | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `fit(X)`           | Compute k-means clustering on dataset `X`.                    |
| `predict(X)`       | Predict the closest cluster for each sample in `X`.           |
| `fit_predict(X)`   | Combines `fit` and `predict` — returns cluster labels.        |
| `fit_transform(X)` | Computes clustering and returns distances to cluster centers. |

---

### 📊 Attributes

| Attribute          | Description                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `cluster_centers_` | Coordinates of cluster centers.                                                                |
| `labels_`          | Cluster labels for each training point.                                                        |
| `inertia_`         | Sum of squared distances of samples to their closest cluster center (used as a cost function). |
| `n_iter_`          | Number of iterations run.                                                                      |

---

### 🧪 Example

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

print("Cluster centers:\n", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
```

---