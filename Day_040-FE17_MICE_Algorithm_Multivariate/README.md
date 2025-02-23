# Day_040 | MICE Algorithm | Multivariate

The MICE (Multiple Imputation by Chained Equations) algorithm is a sophisticated technique for handling missing data in datasets. It's particularly valuable when dealing with multivariate missing data, where missing values occur across multiple columns. Here's a breakdown of the MICE algorithm:

## Core Concepts:
1. Multiple Imputation:
   + Instead of creating a single imputed dataset, MICE generates multiple imputed datasets. This accounts for the uncertainty associated with missing data.
   + By analyzing these multiple datasets, you + obtain more robust statistical results.

2. Chained Equations (Fully Conditional Specification):
    + MICE imputes missing values variable by variable.
    + For each variable with missing values, it builds a prediction model using the other variables in the dataset as predictors.
    + This process is repeated iteratively, with imputed values being updated in each iteration.

## How the MICE Algorithm Works:

1. Initialization:
    - Initially, missing values are filled with temporary estimates (e.g., mean, random values).
2. Iterative Imputation:
    - The algorithm iterates through each variable with missing values.
    - For each variable:
        + It uses the current values of the other variables (including previously imputed values) to build a prediction model.
        + It uses the prediction model to impute the missing values in the current variable.
        + This process is repeated multiple times (iterations).
3. Multiple Datasets:
    - The iterative imputation process is repeated multiple times (m times), creating m complete datasets.
1. Analysis and Pooling:
    - Each of the m imputed datasets is analyzed separately.
    - The results from each analysis are then pooled to obtain overall estimates and standard errors that account for the uncertainty of the missing data.

## Key Advantages of MICE:
1. Flexibility:
    + MICE can handle various data types, including continuous, categorical, and binary variables.
2. Accuracy:
    - It often provides more accurate imputations than simpler methods, as it considers relationships between variables.
3. Uncertainty Handling:
    - By generating multiple imputations, it accounts for the uncertainty associated with missing data.

## Implementation:

1. Python:
    - Scikit-learn's IterativeImputer class can be used to perform MICE-like imputation.
    - There are also other python libraries that are designed to perform MICE.
2. R:
    - The mice package in R is a widely used and powerful implementation of the MICE algorithm.

## Important Considerations:
1. Convergence:
    - It's important to monitor the convergence of the algorithm to ensure that the imputed values stabilize.
2. Model Selection:
    - The choice of prediction models used in the imputation process can impact the results.
3. Computational Cost:
    - MICE can be computationally expensive, especially for large datasets.

## Implementation in Python
> Python | Scikit-Learn

```python
import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression  # Example estimator
from sklearn.ensemble import RandomForestRegressor #Another example estimator

# Create a sample DataFrame with missing values
data = {'A': [1, 2, np.nan, 4, 5, np.nan],
        'B': [7, np.nan, 9, 10, 11, 12],
        'C': [13, 14, 15, np.nan, 17, 18]}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Initialize the IterativeImputer
imputer = IterativeImputer(random_state=0, estimator=LinearRegression()) #you can change the estimator.

# Fit and transform the DataFrame
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nDataFrame after IterativeImputer imputation:\n", df_imputed)

#Example with a different estimator.
imputer2 = IterativeImputer(random_state=0, estimator=RandomForestRegressor())
df_imputed2 = pd.DataFrame(imputer2.fit_transform(df), columns=df.columns)

print("\nDataFrame after IterativeImputer imputation (Random forest estimator):\n", df_imputed2)

#Example with categorical data (needs encoding)
from sklearn.preprocessing import OrdinalEncoder

data2 = {'A': [1, 2, np.nan, 4, 5, 6],
        'B': ['cat', np.nan, 'dog', 'cat', 'bird', 'dog']}
df2 = pd.DataFrame(data2)

encoder = OrdinalEncoder()
df2['B'] = encoder.fit_transform(df2[['B']])

imputer3 = IterativeImputer(random_state=0, estimator=LinearRegression())
df2_imputed = pd.DataFrame(imputer3.fit_transform(df2), columns = df2.columns)

df2_imputed['B'] = encoder.inverse_transform(df2_imputed[['B']])

print("\nDataFrame with categorical data after IterativeImputer imputation:\n",df2_imputed)
```

## Explanation:
1. Import Libraries: Import `pandas`, `numpy`, `IterativeImputer` from `scikit-learn`, and an estimator (like LinearRegression or RandomForestRegressor).
2. Create DataFrame: Create a sample DataFrame with missing values.
3. Initialize Imputer:
    + Create an instance of `IterativeImputer`.
    + `random_state`: Sets the random seed for reproducibility.
    + `estimator`: Specifies the estimator to use for predicting missing values. You can use various regression or classification models here. `LinearRegression` is a common choice for numerical data, and for categorical data after encoding.
4. Fit and Transform: Use `fit_transform()` to fit the imputer to the data and transform the data by imputing missing values. The result is a NumPy array.
5. Create Imputed DataFrame: Convert the NumPy array back into a Pandas DataFrame.
6. Different Estimator: Demonstrates the use of a different estimator, `RandomForestRegressor`.
7. Categorical Data: Demonstrates how to handle categorical data with `IterativeImputer`. Needs ordinal encoding before hand, and decoding after.
8. Output: Print the original and imputed DataFrames.