# Day_015- Working with CSV

## Import Direct CSV

```python
df = pd.read_csv('test.csv')
df.head()
```


## Import using URL
```python
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

df = pd.read_csv(data)
df.head()
```

# Parameter

```
 1. Sep parameter
 2. names
 3. index_col
 4. header
 5. usecols
 6. nrows
 7. skip_bad_line
 8. parse_dates
 9. chunks

 ```