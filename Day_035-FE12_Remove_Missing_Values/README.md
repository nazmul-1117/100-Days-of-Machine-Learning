# Day_035: Handling Missing Values | Remove them | Complete Case Analysis (`CCA`)


## 1. Removing Rows with Missing Values (`dropna()`):
```python
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, np.nan],
        'C': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

df_cleaned = df.dropna()  # Removes rows with ANY NaN
print("Original DataFrame:\n", df)
print("\nDataFrame after dropping rows with NaNs:\n", df_cleaned)

# Drop rows where ALL values are NaN
df_all_nan = df.dropna(how='all')
print("\nDataFrame after dropping rows where ALL values are NaNs:\n", df_all_nan)

# Drop rows based on missing values in specific columns
df_subset = df.dropna(subset=['A', 'B'])
print("\nDataFrame after dropping rows with NaNs in 'A' or 'B':\n", df_subset)
```

## 2. Removing Columns with Missing Values (dropna()):
```python
df_cleaned_cols = df.dropna(axis=1)  # axis=1 for columns
print("\nDataFrame after dropping columns with NaNs:\n", df_cleaned_cols)
```

## Important Considerations:
- **Amount of Missing Data:** If a column has a very high percentage of missing values (e.g., >50%), it might be better to drop the column entirely.
- **Nature of Missing Data:** Is the data `missing completely at random (MCAR)`, `missing at random (MAR)`, or not `missing at random (NMAR)`? This can influence your choice of imputation method. MCAR is ideal for most imputation techniques. If data is NMAR, it can be very difficult to handle missing values appropriately.
- **Impact on Analysis:** Think about how removing or imputing data might affect your analysis or model.
- **Domain Knowledge:** Use your knowledge of the data to guide your decisions.
