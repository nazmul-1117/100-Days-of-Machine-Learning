# Day 121 | Naive Bayes Classifier | Part 4 | Bayes Theorem

---

## 📚 Naive Bayes Theorem

### 📌 What is it?

**Naive Bayes** is a **probabilistic classifier** based on **Bayes’ Theorem** with a strong (naive) assumption that **features are conditionally independent** given the class label.

---

### 🧮 Bayes’ Theorem

Bayes’ Theorem helps us update our beliefs based on new evidence:

$$
P(Y \mid X) = \frac{P(X \mid Y) \cdot P(Y)}{P(X)}
$$

Where:

* $P(Y \mid X)$: Posterior — Probability of class $Y$ given feature $X$
* $P(X \mid Y)$: Likelihood — Probability of feature $X$ given class $Y$
* $P(Y)$: Prior — Probability of class $Y$
* $P(X)$: Evidence — Probability of feature $X$ (same across all classes)

---

### 🧠 Naive Assumption

In Naive Bayes, we assume that **all features are independent given the class**, i.e.,

$$
P(X_1, X_2, ..., X_n \mid Y) = \prod_{i=1}^{n} P(X_i \mid Y)
$$

So the classifier becomes:

$$
P(Y \mid X_1, ..., X_n) \propto P(Y) \cdot \prod_{i=1}^{n} P(X_i \mid Y)
$$

We choose the class $Y$ that **maximizes** this probability (Maximum A Posteriori - MAP estimate).

---

### 📊 Example

Let’s say you're classifying emails as **Spam** or **Not Spam** based on words like “free,” “offer,” and “win.”

Given:

* Prior: $P(\text{Spam}) = 0.6$, $P(\text{Not Spam}) = 0.4$
* Likelihoods: $P(\text{free} \mid \text{Spam}) = 0.8$, $P(\text{free} \mid \text{Not Spam}) = 0.2$

Then you calculate:

$$
P(\text{Spam} \mid \text{free}) \propto 0.6 \cdot 0.8 = 0.48
$$

$$
P(\text{Not Spam} \mid \text{free}) \propto 0.4 \cdot 0.2 = 0.08
$$

So, classify the email as **Spam**.

---

### 📦 Types of Naive Bayes in Scikit-learn

| Type            | Usage                                 |
| --------------- | ------------------------------------- |
| `GaussianNB`    | Continuous features (normal dist.)    |
| `MultinomialNB` | Discrete features (e.g., word counts) |
| `BernoulliNB`   | Binary features (e.g., 0/1 flags)     |

---

### 🐍 Python Code Example

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

X = ["buy cheap meds", "win cash now", "hello friend", "meeting at noon"]
y = [1, 1, 0, 0]  # 1 = Spam, 0 = Not Spam

vec = CountVectorizer()
X_vec = vec.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

test = vec.transform(["win big cash prize"])
print(model.predict(test))  # Output: [1] (Spam)
```

---

### ✅ Summary

* Based on **Bayes’ theorem** with an assumption of **feature independence**
* **Fast**, scalable, and works well with **text classification**
* Easy to implement and often a **strong baseline** model

---