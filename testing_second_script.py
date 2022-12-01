#need to run first testing script first, then link this script to the same console as the first script, then run this script.
df["count_group"] = pd.cut(df["count"], 10)
df.head()