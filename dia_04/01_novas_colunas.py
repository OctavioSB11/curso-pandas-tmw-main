# %%

import pandas as pd
import numpy as np


df = pd.read_csv("../data/clientes.csv", sep=';')
df.head()

# %%
df['pontos_100'] = df['qtdePontos'] + 100
df.head()
# %%

nova_coluna = []
for i in df['qtdePontos']:
    nova_coluna.append(i+100)
    
nova_coluna

# %%
#Verifica se o usuario tem email e tem conta na twitch
df['emailTwitch'] = df['flEmail'] + df['flTwitch']
df.head()

# %%
# Verifica se o usuario tem email ou conta na twitch
df['flEmail'] * df['flTwitch']

# %%
# Verifica qtd de redes sociais de um usuario e cria uma nova coluna
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

# %%
# Verifica se o usuario tem todas as redes sociais e cria uma nova coluna
df["todasSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df

# %%
df['qtdePontos'].describe()

# %%
df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()

# %%
import matplotlib.pyplot as plt

plt.grid(True)
plt.hist(df["logPontos"])
plt.show()