# %%
import pandas as pd
import sqlalchemy
from sklearn import cluster

with open("etl.sql", 'r') as file:
    query = file.read()

print(query)

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

df = pd.read_sql_query(query, con=engine)

df.head()

# %%

# %%
## Treina modelo de cluster
kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[['totalRevenue','totalOrders']])

df["cluster"] =  kmean.labels_
df

# %%
df.to_sql(
    "sellers_cluster",
    con=engine,
    index=False,
    if_exists="replace",
)