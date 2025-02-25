# Day-044 | Winsorization | Percentile-Based Outlier Handling Method
Winsorization, in the context of percentile-based outlier handling, involves replacing extreme values (outliers) with the values at specified percentiles of the data. This effectively "caps" or "floors" the data, limiting the influence of outliers without completely removing them.

## Concept:
1. Percentiles: Percentiles divide a sorted dataset into 100 equal parts. For example, the 5th percentile is the value below which 5% of the data falls.
2. Winsorization: In winsorization, you choose two percentiles (a lower and an upper percentile) and replace any values below the lower percentile with the value at the lower percentile, and any values above the upper percentile with the value at the upper percentile.

## Steps:
1. Choose Percentiles: Select the lower and upper percentiles that define your outlier range. Common choices include:
    - `5th` and 95th percentiles
    - `1st` and 99th percentiles
    - `2.5th` and `97.5th` percentiles
2. Calculate Percentile Values: Calculate the values corresponding to the chosen percentiles.
3. Replace Outliers: Replace any values below the lower percentile value with the lower percentile value, and replace any values above the upper percentile value with the upper percentile value.

> Python
```python
import pandas as pd
import numpy as np

def winsorize_percentiles(data, lower_percentile=0.05, upper_percentile=0.95):
    """
    Winsorizes data using percentile-based capping.

    Args:
        data (pd.Series or np.array): The data to winsorize.
        lower_percentile (float): The lower percentile (e.g., 0.05 for 5th percentile).
        upper_percentile (float): The upper percentile (e.g., 0.95 for 95th percentile).

    Returns:
        pd.Series or np.array: The winsorized data.
    """

    lower_limit = data.quantile(lower_percentile)
    upper_limit = data.quantile(upper_percentile)
    winsorized_data = np.clip(data, lower_limit, upper_limit)
    return winsorized_data

# Example usage:
data = pd.Series([10, 15, 20, 25, 30, 100, -5, -10])

winsorized_data = winsorize_percentiles(data)
print("Original Data:\n", data)
print("\nWinsorized Data:\n", winsorized_data)

#Example with a dataframe.
data2 = {'values' : [10, 15, 20, 25, 30, 100, -5, -10]}
df = pd.DataFrame(data2)

df['winsorized_values'] = winsorize_percentiles(df['values'])
print("\nDataframe with winsorized column:\n", df)

#Example with different percentiles.
winsorized_data2 = winsorize_percentiles(data, lower_percentile=0.01, upper_percentile=0.99)
print("\nWinsorized Data with 1st and 99th percentiles:\n", winsorized_data2)
```