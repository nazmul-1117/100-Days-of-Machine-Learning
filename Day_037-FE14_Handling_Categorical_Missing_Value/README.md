# Day_037-Missing Value Imputation | Categorical Data Impute

There are two way to impute missing value
1. Most Frequent Data `Mode`
2. Using `Missing` word and create a new category

## Most Frequent Data `MODE`
> Pandas
```python
import pandas as pd

df = pd.DataFrame({'category': ['A', 'B', None, 'A', 'C', None, 'A']})
most_frequent = df['category'].mode()[0]  # Get the mode
df['category'].fillna(most_frequent, inplace=True)
print(df)
```

>Scikit-learn
```python
from sklearn.impute import SimpleImputer
import numpy as np

df = pd.DataFrame({'category': ['A', 'B', np.nan, 'A', 'C', np.nan, 'A']})
imputer = SimpleImputer(strategy='most_frequent')
df['category'] = imputer.fit_transform(df[['category']])
print(df)
```

## Creating a New Category ("Missing" or "Unknown"):
>Pandas
```python
df = pd.DataFrame({'category': ['A', 'B', None, 'A', 'C', None, 'A']})
df['category'].fillna('Missing', inplace=True)
print(df)
```

[References_by_Gemini](https://gemini.google.com/app/)
