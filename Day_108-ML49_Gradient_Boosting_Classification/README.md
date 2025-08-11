# Day 108 | Gradient Boosting Mathematics | Classification | Part 3

---

## 🎯 Goal: Binary Classification with Gradient Boosting

We want to predict a binary label $y_i \in \{0, 1\}$ using an additive model:

$$
F_M(x) = F_0(x) + \sum_{m=1}^{M} \gamma_m h_m(x)
$$

Where:

* $F_m(x)$ is the **log-odds** score (not probabilities yet).
* $h_m(x)$ is the m-th weak learner (typically a decision tree).
* $\gamma_m$ is the learning rate or step size.

---

## 🔢 Step-by-Step: Gradient Boosting for Classification

---

### 🔹 Step 1: Define the Loss Function

We use the **Log-Loss (Logistic Loss)**:

$$
L(y, \hat{p}) = -[y \log(\hat{p}) + (1 - y)\log(1 - \hat{p})]
$$

We convert predicted log-odds $F(x)$ to **probabilities** using the sigmoid function:

$$
\hat{p} = \frac{1}{1 + e^{-F(x)}}
$$

---

### 🔹 Step 2: Initialize the Model

Start with a **constant model** that minimizes the loss:

$$
F_0 = \arg\min_\gamma \sum_{i=1}^n L(y_i, \gamma)
$$

For log-loss, the optimal initial log-odds is:

$$
F_0 = \log \left( \frac{\bar{y}}{1 - \bar{y}} \right), \quad \text{where } \bar{y} = \frac{1}{n} \sum y_i
$$

---

### 🔹 Step 3: For Each Boosting Iteration $m = 1, 2, ..., M$

---

#### ✅ Step 3.1: Compute the **Negative Gradient**

This acts as the **pseudo-residual**:

$$
r_{im} = -\left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]
= y_i - \hat{p}_i
$$

This is the difference between actual and predicted probabilities.

---

#### ✅ Step 3.2: Fit a Weak Learner

Train a regression tree $h_m(x)$ on the pseudo-residuals $r_{im}$.

---

#### ✅ Step 3.3: Compute Optimal Step Size $\gamma_m$

For each leaf $j$ in the tree, compute the value to add to predictions in that region:

$$
\gamma_{jm} = \arg\min_\gamma \sum_{x_i \in R_{jm}} L(y_i, F_{m-1}(x_i) + \gamma)
$$

For log-loss, a good approximation (from Friedman, 2001):

$$
\gamma_{jm} = \frac{\sum_{x_i \in R_{jm}} r_{im}}{\sum_{x_i \in R_{jm}} \hat{p}_i (1 - \hat{p}_i)}
$$

---

#### ✅ Step 3.4: Update the Model

Update the prediction function for each region $R_{jm}$:

$$
F_m(x) = F_{m-1}(x) + \gamma_{jm} \quad \text{if } x \in R_{jm}
$$

Repeat for $M$ iterations.

---

### 🔚 Step 4: Make Predictions

After training, convert the final **log-odds** to probabilities:

$$
\hat{p}(x) = \frac{1}{1 + e^{-F_M(x)}}
$$

Then apply a threshold (e.g., 0.5) to get binary predictions.

---

## 🧠 Summary Table

| Step       | What it does                               |
| ---------- | ------------------------------------------ |
| Initialize | Set $F_0$ using log-odds of positive class |
| Residual   | $r_i = y_i - \hat{p}_i$                    |
| Tree fit   | Fit tree on $r_i$                          |
| Update     | Adjust leaf outputs by optimal $\gamma$    |
| Repeat     | Until max iterations                       |

---

## Refrences
[Blog](https://towardsdatascience.com/all-you-need-to-know-about-gradient-boosting-algorithm-part-2-classification-d3ed8f56541e/)

[ChatGPT](None)

---
