# Day_043 | Outlier Detect | IQR method

The `Interquartile Range (IQR)` method is a robust statistical approach for detecting outliers in a dataset. It's less sensitive to extreme values than the Z-score method, making it particularly useful for `skewed distributions`. Here's a detailed explanation:

1. Understanding the IQR:
Quartiles: The IQR is based on quartiles, which divide a sorted dataset into four equal parts:
    - **Q1 (25th percentile):** The value below which `25%` of the data falls.   
    - **Q2 (50th percentile or median):** The value below which `50%` of the data falls.   
    - **Q3 (75th percentile):** The value below which `75%` of the data falls
2. **IQR Calculation:** The IQR is the difference between the third quartile (Q3) and the first quartile (Q1): `IQR = Q3 - Q1`.   

## Identifying Outliers Using the IQR:
- **Lower Bound:** Data points below `Q1 - 1.5 * IQR` are considered potential outliers.   
- **Upper Bound:** Data points above `Q3 + 1.5 * IQR` are considered potential outliers.   
- The `1.5 Factor`: The 1.5 factor is a common convention. It defines a reasonable range for typical data points. You can adjust this factor (e.g., using 3.0 for more extreme outliers) if needed.

>Python
```python
import pandas as pd
import numpy as np

def detect_outliers_iqr(data):
    """
    Detects outliers using the IQR method.

    Args:
        data (pd.Series or np.array): The data to analyze.

    Returns:
        pd.Series: A boolean Series indicating outliers (True) or not (False).
    """

    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (data < lower_bound) | (data > upper_bound)
    return outliers

# Example usage:
data = pd.Series([10, 15, 20, 25, 30, 100])

outliers = detect_outliers_iqr(data)
print("Outliers:\n", data[outliers])

#Example with a dataframe
data2 = {'values' : [10, 15, 20, 25, 30, 100]}
df = pd.DataFrame(data2)

df['outlier'] = detect_outliers_iqr(df['values'])
print("\nDataframe with outlier column:\n", df)

#Example of capping data to the upper and lower bounds.
lower_limit = data.quantile(0.25) - 1.5 * (data.quantile(0.75) - data.quantile(0.25))
upper_limit = data.quantile(0.75) + 1.5 * (data.quantile(0.75) - data.quantile(0.25))

capped_data = np.clip(data, lower_limit, upper_limit)

print("\nCapped Data:\n", capped_data)
```

