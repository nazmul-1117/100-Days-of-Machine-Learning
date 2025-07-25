# Day 102 | Bagging vs Boosting

## Key Points
1. Types of Model used
   1. Bagging - `LB`, `HV`
   2. Boosting - `HB` `LV`
2. Sequential vs Parallel
   1. Bagging - `Parallel`
   2. Boosting - `Sequential`
3. Weightage of base Learners
   1. Bagging - `Same Weighted`
   2. Boosting - `Alpha`


---

## 🆚 Bagging vs Boosting

| Aspect               | **Bagging**                                      | **Boosting**                                                  |
| -------------------- | ------------------------------------------------ | ------------------------------------------------------------- |
| **Full Form**        | Bootstrap Aggregating                            | —                                                             |
| **Goal**             | Reduce **variance**                              | Reduce **bias** (and also variance)                           |
| **Learner Type**     | Trains multiple **strong, independent** learners | Trains multiple **weak, sequential** learners                 |
| **Training Process** | Learners trained **in parallel**                 | Learners trained **sequentially**                             |
| **Sample Strategy**  | Uses **random subsets** of the training data     | Each new learner focuses on **mistakes** of the previous ones |
| **Weighting**        | All learners are **equally weighted**            | Learners are **weighted by performance**                      |
| **Overfitting**      | Helps to **prevent** overfitting                 | May **overfit** if not properly regularized                   |
| **Example Models**   | Random Forest                                    | AdaBoost, Gradient Boosting, XGBoost                          |
| **Complexity**       | Simpler and easier to parallelize                | More complex, often achieves higher accuracy                  |

---

## ✅ Summary

* **Bagging** (like Random Forest): Reduces variance by combining predictions of diverse models trained on bootstrapped samples.
* **Boosting** (like AdaBoost): Builds an ensemble **sequentially**, where each model corrects the errors of the previous ones.

---
