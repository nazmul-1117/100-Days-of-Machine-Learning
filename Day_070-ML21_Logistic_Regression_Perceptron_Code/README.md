# Day 70 | Logistic Regression | Perceptron Trick | Code Implementation
The "perceptron trick" in the context of logistic regression refers to a method of iteratively adjusting the decision boundary (line) based on misclassified points, similar to how the perceptron algorithm works, but with the added ability to predict probabilities using a sigmoid function. 

## Perceptron Algorithm:
The perceptron algorithm is a simple linear classifier that aims to find a line (or hyperplane in higher dimensions) that separates data points belonging to different classes. It works by iteratively adjusting the line based on misclassified points, moving the line towards the misclassified point. 

## Iterative Process:
- Start with a line (or hyperplane). 
- Pick a random data point and check if it's correctly classified. 
- If misclassified: Adjust the line towards the misclassified - point. 
- If correctly classified: Do nothing. 
- Repeat until convergence (or a stopping criterion is met). 