# Day 126 | Naive Bayes Classifier | Part 9 | Bayes Theorem | Handling Numarical Data

Great question! If you have **numerical data** (like height and weight), and you want to classify a categorical label (like gender: Male or Female), you can use **Gaussian Naive Bayes**, which assumes that **numerical features follow a normal distribution** within each class.

---

## 🎯 Problem Setup

Suppose your dataset looks like this:

| Height (cm) | Weight (kg) | Gender |
| ----------- | ----------- | ------ |
| 180         | 80          | Male   |
| 165         | 55          | Female |
| 170         | 60          | Female |
| 175         | 75          | Male   |
| ...         | ...         | ...    |

Now, given a new input (e.g., Height = 168, Weight = 58), you want to **predict Gender**.

---

## 🧠 Step-by-Step with Gaussian Naive Bayes

Certainly! Based on the **previous example**, the data has:

* **3 Male samples**
* **3 Female samples**
* **Total samples = 6**

So, the corrected equation for prior probabilities becomes:

---

### 1. **Estimate Prior Probabilities**

$$
P(\text{Male}) = \frac{3}{6} = 0.5, \quad P(\text{Female}) = \frac{3}{6} = 0.5
$$

---

You can also write it generically and then plug in the values like this:

$$
P(\text{Male}) = \frac{3}{3 + 3}, \quad P(\text{Female}) = \frac{3}{3 + 3}
$$



---

### 2. **Estimate Likelihoods Using Gaussian PDF**

Assume each numerical feature is **normally distributed** for each class.

For each class (Male/Female), and each feature (Height, Weight):

$$
P(x_i \mid \text{class}) = \frac{1}{\sqrt{2\pi \sigma^2}} \cdot \exp\left( -\frac{(x_i - \mu)^2}{2\sigma^2} \right)
$$

Where:

* $\mu$: mean of the feature for that class
* $\sigma^2$: variance of the feature for that class
* $x_i$: the observed feature value

---

### 3. **Apply Naive Bayes Formula**

$$
P(\text{Male} \mid X) \propto P(\text{Male}) \cdot P(\text{Height} \mid \text{Male}) \cdot P(\text{Weight} \mid \text{Male})
$$

$$
P(\text{Female} \mid X) \propto P(\text{Female}) \cdot P(\text{Height} \mid \text{Female}) \cdot P(\text{Weight} \mid \text{Female})
$$

Then, choose the class with the higher probability.

---

## 🐍 Python Example (Manual)

```python
import numpy as np
from math import pi, exp, sqrt

# Sample data: [height, weight]
male_data = np.array([[180, 80], [175, 75], [178, 78]])
female_data = np.array([[165, 55], [160, 50], [170, 60]])

# Step 1: Compute priors
P_male = len(male_data) / (len(male_data) + len(female_data))
P_female = 1 - P_male

# Step 2: Compute mean and std for each feature
male_mean = np.mean(male_data, axis=0)
male_std = np.std(male_data, axis=0)
female_mean = np.mean(female_data, axis=0)
female_std = np.std(female_data, axis=0)

# Gaussian probability function
def gaussian(x, mean, std):
    return (1 / (sqrt(2 * pi) * std)) * exp(-((x - mean) ** 2) / (2 * std ** 2))

# New sample to predict
X = np.array([168, 58])

# Step 3: Compute likelihoods
likelihood_male = np.prod([gaussian(x, m, s) for x, m, s in zip(X, male_mean, male_std)])
likelihood_female = np.prod([gaussian(x, m, s) for x, m, s in zip(X, female_mean, female_std)])

# Step 4: Compute posteriors (unnormalized)
posterior_male = P_male * likelihood_male
posterior_female = P_female * likelihood_female

# Step 5: Predict
prediction = 'Male' if posterior_male > posterior_female else 'Female'
print("Prediction:", prediction)
```

---

## ✅ Use Scikit-Learn (Simplified)

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

# Sample data
X = np.array([
    [180, 80],
    [175, 75],
    [178, 78],
    [165, 55],
    [160, 50],
    [170, 60]
])
y = np.array(['Male', 'Male', 'Male', 'Female', 'Female', 'Female'])

# Train model
model = GaussianNB()
model.fit(X, y)

# Predict
new_sample = np.array([[168, 58]])
prediction = model.predict(new_sample)
print("Predicted Gender:", prediction[0])
```

---

## 🎓 Summary

* Use **Gaussian Naive Bayes** for numerical features.
* It fits a **normal distribution per feature per class**.
* You can do this manually or with `sklearn.naive_bayes.GaussianNB`.