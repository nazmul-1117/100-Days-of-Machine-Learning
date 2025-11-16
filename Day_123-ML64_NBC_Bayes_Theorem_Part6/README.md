# Day 123 | Naive Bayes Classifier | Part 6 | Bayes Theorem | Example

---

## 🏏 Cricket Example: Predicting Match Outcome Based on Toss Win

### 🎯 Scenario

A cricket analyst is trying to predict whether **Team A will win** a match, given that they **won the toss**.

From historical data:

* **Team A wins 70%** of the matches when they **win the toss**
  $P(\text{Win} \mid \text{TossWin}) = 0.70$

* **Team A wins 40%** of the matches when they **lose the toss**
  $P(\text{Win} \mid \text{TossLose}) = 0.40$

* The probability of **winning the toss** is 50%
  $P(\text{TossWin}) = 0.5$

You’re told that Team A **won** the match. What is the **probability that they had won the toss**?

---

### ✅ Goal

Find:

$$
P(\text{TossWin} \mid \text{Win})
$$

---

### 🧮 Apply Bayes’ Theorem

$$
P(\text{TossWin} \mid \text{Win}) = \frac{P(\text{Win} \mid \text{TossWin}) \cdot P(\text{TossWin})}{P(\text{Win})}
$$

---

### Step 1: Compute Total Probability of Winning the Match

$$
P(\text{Win}) = P(\text{Win} \mid \text{TossWin}) \cdot P(\text{TossWin}) + P(\text{Win} \mid \text{TossLose}) \cdot P(\text{TossLose})
$$

$$
= (0.70 \cdot 0.5) + (0.40 \cdot 0.5) = 0.35 + 0.20 = 0.55
$$

---

### Step 2: Apply Bayes’ Theorem

$$
P(\text{TossWin} \mid \text{Win}) = \frac{0.70 \cdot 0.5}{0.55} = \frac{0.35}{0.55} \approx 0.636
$$

---

### 🎉 Final Answer:

If Team A wins the match, there is a **63.6% chance they also won the toss**.

---

### 🐍 Python Code

```python
P_win_given_tosswin = 0.70
P_win_given_tosslose = 0.40
P_tosswin = 0.5
P_tosslose = 0.5

P_win = (P_win_given_tosswin * P_tosswin) + (P_win_given_tosslose * P_tosslose)

P_tosswin_given_win = (P_win_given_tosswin * P_tosswin) / P_win
print(f"Probability that Team A won the toss given they won the match: {P_tosswin_given_win:.3f}")
# Output: 0.636
```

---

### 🏁 Insight:

Even though toss might seem minor, **Bayes' Theorem reveals how prior data impacts our belief** — here, that winning the toss increases chances of winning the match.