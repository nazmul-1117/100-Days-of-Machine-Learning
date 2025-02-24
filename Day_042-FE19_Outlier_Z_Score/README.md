# Day 042 | Outlier | Z-Score
The Z-score (also called the standard score) measures how many standard deviations a data point is away from the mean of the distribution.

It's calculated using the formula: `Z = (X - μ) / σ` </br>
where:
- `X` is the data point.
- `μ` is the mean of the distribution.
- `σ` is the standard deviation of the distribution.

## How Z-Scores Relate to Outliers:
1. Identifying Extreme Values: Z-scores help identify extreme values in a dataset. A large absolute Z-score indicates that a data point is far from the mean, suggesting it might be an outlier.
2. In a normal distribution, approximately:
    - `68%` of the data falls within `±1` standard deviation (Z-score ±1).
    - `95%` of the data falls within `±2` standard deviations (Z-score ±2).
    - `99.7%` of the data falls within `±3` standard deviations (Z-score ±3).
Therefore, values with Z-scores beyond ±3 are considered relatively rare.

## Range
```
1.  68.2% {
            μ + σ
            μ - σ 
          }
2. 95% {
            μ + 2σ
            μ - 2σ
        }

3. 99.7% {
            μ + 3σ
            μ - 3σ
        }
```

## Capping Concept
```cpp
    if(df["cgpa"] > upper_limit){
        df["cgpa"] = upper_limit;
    }
    else{
        if(df["cgpa"] < lower_limit){
            df["cgpa"] = lower_limit;
        }
        else{
            df["cgpa"] = df["cgpa"]
        }
    }
```