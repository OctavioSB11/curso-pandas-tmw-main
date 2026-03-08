# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%
# Filtrando de forma tradicional
pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])


resultado
filtro

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)

filtro = brinquedo["idade"] >= 18 # compara cada uma das idades e retorna uma serie com tipo bool com os elementos que tinha em 'idade'
brinquedo[filtro] # usa o filtro que fizemos anteriormente e aplica no df, retornando apenas os True

# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=';')
df.head()

# %%
# Valores maiores que 50
filtro = df['QtdePontos'] >= 50
df[filtro]
# %%
# Valores entre 50 e 100
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)
df[filtro]
# %%
# Valores exatos, retorna apenas 1 OU 100
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]
# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"]<=50) | (df["dtCriacao"]>='2025-01-01')
df[filtro]