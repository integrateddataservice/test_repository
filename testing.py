import pandas as pd
#!pip install pandas-gbq

query =     """
SELECT name, SUM(number) as count
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    GROUP BY name
    ORDER BY count DESC
    LIMIT 10
"""

#df = pd.read_gbq(query)

#df.head()

from google.cloud import bigquery

client = bigquery.Client()#location="europe-west2")

query_job = eu_client.query(query)

df = query_job.to_dataframe()
df

eu_client = bigquery.Client(location="europe-west2")

project_id = 'ons-ids-analysis-uat'

table_id = 'ons-ids-analysis-uat.uat-wip-notebook.test_wil'

import pandas_gbq

pandas_gbq.to_gbq(df, table_id, project_id=project_id)

query = "select * from `ons-ids-analysis-uat.uat-wip-notebook.penguins`"

