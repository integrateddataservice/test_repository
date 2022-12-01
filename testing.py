import pandas as pd
!pip install pandas-gbq

df = pd.read_gbq(
    """SELECT name, SUM(number) as count
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    GROUP BY name
    ORDER BY count DESC
    LIMIT 10""")

df.head()