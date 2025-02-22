# Day_038-Random value Imputation | Missing Indicator | Automatically Select value

## 1. Random Value Imputation
### How Random Value Imputation Works:
- **Identify Missing Values:** First, you identify the missing values (NaNs) in the column you want to impute.
- **Sample from Non-Missing Values:** You randomly select values from the set of non-missing values in the same column.
- **Replace Missing Values:** You replace each missing value with one of the randomly selected values.

>Pandas
```python
import pandas as pd
import numpy as np

def random_imputation(df, feature):
    """
    Imputes missing values in a column with random values from the same column.

    Args:
        df (pd.DataFrame): The DataFrame containing the missing values.
        feature (str): The name of the column to impute.

    Returns:
        pd.DataFrame: The DataFrame with imputed values.
    """

    missing_mask = df[feature].isnull()
    non_missing_values = df[feature].dropna().values
    df.loc[missing_mask, feature] = np.random.choice(non_missing_values, size=missing_mask.sum())
    return df

# Example usage:
data = {'A': [1, 2, np.nan, 4, 5, np.nan, 7],
        'B': ['cat', 'dog', np.nan, 'cat', 'bird', 'dog', np.nan]}
df = pd.DataFrame(data)

df = random_imputation(df, 'A')
df = random_imputation(df, 'B')

print(df)
```
## Automatically Imputation Missing Value
### 1. Basic Heuristics:
- Data Type:
    - Numerical:
        + If the data is normally distributed and outliers are not a major concern, use mean imputation.
        + If the data is skewed or outliers are present, use median imputation.
        + If the data has a trend, use interpolation.
    - Categorical:
        - If the categories are balanced, use mode imputation.
        - If missingness is potentially informative, create a "Missing" or "Unknown" category.
- Percentage of Missing Data:
    - If the percentage of missing data in a column is very high (e.g., > 50%), consider dropping  the column.
    - If the percentage is low (e.g., < 5%), simple imputation methods (mean, median, mode) might be sufficient.
    - If the percentage is between 5% and 50%  investigate further, and consider more  - advanced imputation methods.
- Correlation:
    - If there are strong correlations between features, use predictive imputation (e.g., KNN imputation or model-based imputation).
    - If there are weak correlations, simple imputation methods might be sufficient.

### 2. Automated Techniques:
- Machine Learning Based Imputation:
    + KNN Imputation: Use sklearn.impute.KNNImputer. It automatically selects the nearest neighbors to impute missing values.
    + Iterative Imputation (sklearn.impute.IterativeImputer): This method models each feature with missing values as a function of other features and uses that estimate for imputation. It can handle various data types.
- Automated Feature Selection:
    - Before imputation, use feature selection techniques (e.g., correlation analysis, feature importance from tree-based models) to identify features that are strongly related to the features with missing values. This can guide your choice of imputation method.

- Cross-Validation:
    - Use cross-validation to evaluate the performance of different imputation methods.
    - Split your data into training and validation sets.
    - Apply different imputation methods to the training set.
    - Evaluate the performance of your model on the validation set.
    - Select the imputation method that yields the best performance.
- Libraries for Automated Imputation:
    - missingno: This library provides visualizations to help you understand missing data patterns.
    - autoimpute: Provides automated imputation strategies.