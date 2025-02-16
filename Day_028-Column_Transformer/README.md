# Day_028-Column Transformer

Column Transformer in scikit-learn is a powerful tool for preprocessing data, especially when you have a mix of different data types (numerical, categorical, etc.) that require different preprocessing steps.  It allows you to apply specific transformations to individual columns or groups of columns and then combine the results into a single array that can be fed into a machine learning model.

## Key Benefits:
- **Organization:** Keeps your preprocessing code clean and organized, especially when dealing with many features and different transformation needs.
- **Flexibility:** Apply different transformers (scalers, encoders, etc.) to different columns.
- **Pipeline Integration:** Seamlessly integrates with scikit-learn pipelines, making it easy to automate your entire machine learning workflow.

## How it Works:
You define a ColumnTransformer object, specifying:

- **Transformers:** The preprocessing steps you want to apply (e.g., `StandardScaler`, `OneHotEncoder`).
- **Columns:** The columns to which each transformer should be applied. You can specify column names, indices, or use selectors like `make_column_selector` (for selecting columns based on data type).
- **"remainder":** How to handle columns not explicitly specified. Options include "`drop`" (remove), "`passthrough`" (keep unchanged), or a transformer to apply to the remaining columns.

## Code:

```python

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Sample Data (Illustrative)
X = [['numerical1', 'categorical1'], ['numerical2', 'categorical2'], ...]  # Your data
y = [...] # Your target variable

# Define the ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['numerical_column_name']),  # Scale numerical columns
        ('cat', OneHotEncoder(), ['categorical_column_name'])   # One-hot encode categorical columns
    ],
    remainder='passthrough'  # Keep other columns as they are
)

# Create a pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())  # Your model
])

# Fit and use the pipeline
pipeline.fit(X, y)
predictions = pipeline.predict(X_new)

```