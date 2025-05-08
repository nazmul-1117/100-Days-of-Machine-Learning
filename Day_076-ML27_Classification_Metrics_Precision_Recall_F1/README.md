# Day 076 | Classification Metrics | Logistic Regression | Classification | Precision | Recall | F1

## 1. Precision (Positive Predictive Value):
`Precision` is the proportion of all the model's *positive classifications* that are *actually positive*.

- **Definition:** The proportion of correctly predicted positive instances out of all instances predicted as positive. It answers - **the question:** "Of all the instances the model labeled as positive, how many were actually positive?"
- **Formula:** Precision = True Positives / (True Positives + False Positives)
- **Pros:** Useful when the cost of a false positive is high (e.g., in spam detection, we want to be sure an email is spam before marking it as such).
- **Question:** What Proportion of `Actual Positive` is `Truly Positive`?

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mtext>Precision</mtext>
  <mo>=</mo>
  <mfrac>
    <mtext>correctly classified actual positives</mtext>
    <mtext>everything classified as positive</mtext>
  </mfrac>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <mi>T</mi>
      <mi>P</mi>
    </mrow>
    <mrow>
      <mi>T</mi>
      <mi>P</mi>
      <mo>+</mo>
      <mi>F</mi>
      <mi>P</mi>
    </mrow>
  </mfrac>
</math>



## 2. Recall (Sensitivity, True Positive Rate):
The `True Positive Rate (TPR)`, or the proportion of all *actual positives* that were classified *correctly as positives*, is also known as `Recall`.

- **Definition:** The proportion of correctly predicted positive instances out of all actual positive instances. It answers the - **question:** "Of all the actual positive instances, how many did the model correctly identify?"   
- **Formula:** Recall = True Positives / (True Positives + False Negatives)   
- **Pros:** Useful when the cost of a false negative is high (e.g., in medical diagnosis, we want to avoid missing any actual positive cases).
- **Question:** What Proportion of `Actual Positive` is `Correctly Classified`?

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mtext>Recall (or TPR)</mtext>
  <mo>=</mo>
  <mfrac>
    <mtext>correctly classified actual positives</mtext>
    <mtext>all actual positives</mtext>
  </mfrac>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <mi>T</mi>
      <mi>P</mi>
    </mrow>
    <mrow>
      <mi>T</mi>
      <mi>P</mi>
      <mo>+</mo>
      <mi>F</mi>
      <mi>N</mi>
    </mrow>
  </mfrac>
</math>


## 3. F1 Score
The F1 score is the harmonic mean (a kind of average) of precision and recall.

- **Definition:** The `Harmonic Mean` of precision and recall. It provides a balanced measure of a model's performance, especially when there is an uneven class distribution.   
- **Formula:** F1-Score = 2 * (Precision * Recall) / (Precision + Recall)
- **Pros:** Considers both false positives and false negatives. Useful when you want a balance between precision and recall.

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mtext>F1</mtext>
  <mo>=</mo>
  <mn>2</mn>
  <mo>&#x2217;<!-- ∗ --></mo>
  <mfrac>
    <mtext>precision * recall</mtext>
    <mtext>precision + recall</mtext>
  </mfrac>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <mn>2</mn>
      <mtext>TP</mtext>
    </mrow>
    <mrow>
      <mn>2</mn>
      <mtext>TP + FP + FN</mtext>
    </mrow>
  </mfrac>
</math>