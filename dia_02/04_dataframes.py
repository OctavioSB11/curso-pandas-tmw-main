# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.head()

# %%
df_clientes.tail()

# %%
df_clientes.sample()
# %%
df_clientes.shape

# %%
df_clientes.columns

# %%
df_clientes.index


# %%
df_clientes.info(memory_usage='deep')


# %%
#retorna uma sério com a tipagem de cada coluna
df_clientes.dtypes