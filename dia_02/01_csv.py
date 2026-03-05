# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%

df.to_csv('clientes.csv', index=False)

# %%

df.to_csv('clientes.parquet', index=False)

df_2 = pd.read_parquet('clientes.parquet')


# %%
df.to_excel("clientes.xlsx", index=False)

df_3 = pd.read_excel("clientes.xlsx")
df_3

# %%
df_ex = pd.read_csv("../data/exemplo_sep.csv", sep=";")
df_ex
# %%
