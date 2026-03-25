# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%

clientes.dropna(how="any")

# %%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

# df
df.dropna(how="all", subset=["idade", "nome"])

# %%

df["idade"] = df["idade"].fillna(0)
df

# %%
# preenche NaN da coluna nome como alguém e da coluna idade como 0
df.fillna({"nome": "alguem", "idade": 0})

# %%
medias = df[['idade', 'salario']].mean()
df.fillna(medias)

# %%

df["idade"].fillna(df["idade"].mean()).mean()