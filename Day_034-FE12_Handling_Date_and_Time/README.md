# Day_034-Handling Dates and Times
"Handling date and time" refers to `the process of accurately storing, manipulating, and displaying date and time values in a computer system`, often involving practices like using consistent formats (like ISO 8601), considering time zones, and utilizing appropriate data types to ensure proper calculations and comparisons between dates and times. 

## Key aspects of handling date and time:
### Consistent format:
Choosing a standard format like ISO 8601 (`YYYY-MM-DD` for date, `HH:MM:SS` for time) to avoid ambiguity and facilitate data exchange across systems


## 1. Converting to Datetime:
`pd.to_datetime()`: This is the primary function for converting strings or other representations to datetime objects.

>Python
```python
import pandas as pd

dates = ['2023-10-26', '10/26/2023', 'Oct 26, 2023']  # Different formats
datetimes = pd.to_datetime(dates)
print(datetimes)

# Handling different formats with 'format' argument
datetimes_formatted = pd.to_datetime(['26-10-2023'], format='%d-%m-%Y')
print(datetimes_formatted)

# Handling errors
datetimes_errors = pd.to_datetime(['2023-10-26', 'Invalid Date'], errors='coerce') # 'coerce' sets invalid parsing to NaT (Not a Time)
print(datetimes_errors)

# From Unix timestamps
timestamps = [1677888000, 1677974400]  # Unix timestamps in seconds
datetimes_timestamps = pd.to_datetime(timestamps, unit='s')
print(datetimes_timestamps)
```

## 2. Accessing Date and Time Components:
Once you have datetime objects, you can easily access individual components:
>Python
```python
date_series = pd.to_datetime(['2023-10-26', '2024-01-15'])

print(date_series.dt.year)
print(date_series.dt.month)
print(date_series.dt.day)
print(date_series.dt.hour)
print(date_series.dt.minute)
print(date_series.dt.second)
print(date_series.dt.weekday)  # Monday=0, Sunday=6
print(date_series.dt.dayofyear)
print(date_series.dt.weekofyear)  # or .isocalendar().week
print(date_series.dt.quarter)
print(date_series.dt.time)  # Time part
print(date_series.dt.date)  # Date part
```
## 3. Time Zones:
Pandas supports time zones:
>Python
```python
datetimes_tz = pd.to_datetime(['2023-10-26']).tz_localize('UTC').tz_convert('US/Eastern')
print(datetimes_tz)
```

## 4. Date and Time Arithmetic:
You can perform arithmetic operations on datetime objects:
>Python
```python
date1 = pd.to_datetime('2023-10-26')
date2 = pd.to_datetime('2023-11-02')

time_difference = date2 - date1
print(time_difference)  # Output: 7 days 00:00:00

# Adding or subtracting time deltas
new_date = date1 + pd.Timedelta(days=7)
print(new_date)
```

## 5. Time Series Indexing and Slicing:
You can use datetimes as the index of a Pandas Series or DataFrame, enabling powerful time-based indexing and slicing:
>Python
```python
dates = pd.date_range('2023-10-26', periods=5)  # Create a date range
series = pd.Series(range(5), index=dates)

print(series['2023-10-27'])  # Access a specific date
print(series['2023-10-26':'2023-10-28'])  # Slice a date range
```
## 6. Resampling:
Resampling allows you to change the frequency of your time series data:
>Python
```python
# Assuming 'series' from the previous example
daily_data = series.resample('D').sum() # Daily data
weekly_data = series.resample('W').sum() # Weekly data
monthly_data = series.resample('M').sum() # Monthly data
print(weekly_data)
```
## 7. Working with Time Deltas:
pd.Timedelta objects represent differences between times:
>Python
```python
time_diff = pd.Timedelta('2 days 3 hours 4 minutes')
print(time_diff)
```
## 8. String Formatting:
You can format datetime objects into strings:
>Python
```python
now = pd.to_datetime('today')
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)
```

## 9. Common Time Series Functions:
- `pd.date_range():` Generates a sequence of dates.
- `pd.bdate_range():` Generates a sequence of business dates (excluding weekends).
- `pd.offsets:` Provides various date and time offsets (e.g., pd.offsets.Day, pd.offsets.MonthEnd).