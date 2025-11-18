# Day 124 | Naive Bayes Classifier | Part 7 | Bayes Theorem | Example

---

## 📘 Naive Bayes Classifier — Detailed Mathematical Explanation

---

### ✅ 1. **Bayes’ Theorem (Base Formula)**

For a given class $C$ and feature vector $X$, Bayes' Theorem says:

$$
P(C \mid X) = \frac{P(X \mid C) \cdot P(C)}{P(X)}
$$

Where:

* $P(C \mid X)$: Posterior probability of class $C$ given feature vector $X$
* $P(X \mid C)$: Likelihood of feature vector $X$ given class $C$
* $P(C)$: Prior probability of class $C$
* $P(X)$: Evidence (total probability of features)

---

### ✅ 2. **Naive Assumption (Conditional Independence)**

Assume the features $X = (x_1, x_2, ..., x_n)$ are **conditionally independent** given class $C$:

$$
P(X \mid C) = P(x_1, x_2, ..., x_n \mid C) = \prod_{i=1}^{n} P(x_i \mid C)
$$

This is the **"naive"** part of Naive Bayes.

---

### ✅ 3. **Naive Bayes Classifier Formula**

Plug into Bayes’ Theorem:

$$
P(C \mid X) = \frac{P(C) \cdot \prod_{i=1}^{n} P(x_i \mid C)}{P(X)}
$$

* We ignore $P(X)$ because it's the same for all classes (used only for normalization).

So we compute the **unnormalized posterior**:

$$
\hat{P}(C \mid X) \propto P(C) \cdot \prod_{i=1}^{n} P(x_i \mid C)
$$

And we classify by:

$$
\hat{C} = \arg\max_{C} \; P(C) \cdot \prod_{i=1}^{n} P(x_i \mid C)
$$

---

### ✅ 4. **Handling Different Feature Types**

#### A. **Multinomial Naive Bayes**

Used for discrete counts (e.g. text classification).

* Feature $x_i$ is the count of word $i$ in the document.
* Use frequency likelihood:

$$
P(x_i \mid C) = \frac{N_{i,C} + \alpha}{N_C + \alpha d}
$$

Where:

* $N_{i,C}$: Number of times feature $i$ appears in class $C$
* $N_C$: Total count of all features in class $C$
* $d$: Number of features (vocabulary size)
* $\alpha$: Laplace smoothing parameter (usually $\alpha = 1$)

#### B. **Gaussian Naive Bayes**

Used for continuous data. Assume feature $x_i$ follows normal distribution for class $C$:

$$
P(x_i \mid C) = \frac{1}{\sqrt{2\pi\sigma_{i,C}^2}} \cdot \exp\left( -\frac{(x_i - \mu_{i,C})^2}{2\sigma_{i,C}^2} \right)
$$

Where:

* $\mu_{i,C}$: Mean of feature $x_i$ in class $C$
* $\sigma_{i,C}^2$: Variance of feature $x_i$ in class $C$

#### C. **Bernoulli Naive Bayes**

Used for binary features (0/1 presence of words):

$$
P(x_i \mid C) = p_{i,C}^{x_i} \cdot (1 - p_{i,C})^{(1 - x_i)}
$$

Where $p_{i,C}$ is the probability of feature $i$ being 1 in class $C$.

---

### ✅ 5. **Log Transformation to Avoid Underflow**

Since multiplying many small probabilities can cause numerical underflow, we use **log probabilities**:

$$
\log P(C \mid X) \propto \log P(C) + \sum_{i=1}^{n} \log P(x_i \mid C)
$$

Then choose the class with the highest score:

$$
\hat{C} = \arg\max_{C} \left[ \log P(C) + \sum_{i=1}^{n} \log P(x_i \mid C) \right]
$$

---

### ✅ Summary Table

| Component      | Formula                                                 |
| -------------- | ------------------------------------------------------- |
| Posterior      | $P(C \mid X)$                                           |
| Prior          | $P(C)$                                                  |
| Likelihood     | $\prod_{i} P(x_i \mid C)$                               |
| Evidence       | $P(X)$, ignored in classification                       |
| Final decision | $\hat{C} = \arg\max_C P(C) \cdot \prod_i P(x_i \mid C)$ |

---

### ✅ Real Use Case in Text Classification

In spam filtering:

* Classes: **Spam**, **Not Spam**
* Features: word counts in an email
* Compute prior from dataset (e.g. % of spam emails)
* Compute word probabilities per class
* Predict using the Naive Bayes rule

---


