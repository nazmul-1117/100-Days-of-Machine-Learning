# Day_017-Data Fetch from API

Analytics professionals often find themselves working with data that is present outside the traditional databases, some of this data is structured (CSV Files, Parquet files, Arrow files, Spark systems), some are semi-structured (JSON’s), and other times totally unstructured (Raw Text documents, Images, etc.). Many startups and even established companies either lack a data engineer function or the data engineers are overwhelmed with their tasks that the data analysts/scientists are obliged to do some of the engineer’s functions. [link](https://medium.com/analytics-lane/python-get-and-process-web-api-data-through-pandas-and-requests-part-1-32127638b463)


## Here some steps to fetch data from API

### Step_1
```python
# import the libraries
import requests
from pandas import json_normalize

# declare the url of the web api
url = "https://xxxx-api-layer.xxxxx.xx/listDiscount"

```

### Step_2
```python
response = requests.get(url)
```

### Step_3
```python
df = pd.DataFrame(response.json()['results'])[column_list]
```


