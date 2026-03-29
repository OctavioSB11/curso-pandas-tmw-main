# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=';')
df.head()

# %%
def get_last_id(x):
    return x.split("-")[-1]

# %%

id_novo = []

for i in df['idCliente']:
    id_formatado = get_last_id(i)
    id_novo.append(id_formatado)

df['novo_id'] = id_novo
df.head()

# %%
# Usamos o .apply para aplicar uma função em todos os elementos de uma série
df['idCliente'].apply(get_last_id)