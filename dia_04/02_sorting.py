# %%

import pandas as pd
import numpy as np


clientes = pd.read_csv("../data/clientes.csv", sep=';')
clientes.head()

max_pontos = clientes['qtdePontos'].max()
filtro = clientes['qtdePontos'] == max_pontos
clientes[filtro]

# %%
# Ordena a o df de acordo com a ordenação da serie de qtdePonto, usando o filtro do maior para o menor
# Retornando então os 5 maiores pontuadores
top_5 = (clientes.sort_values(by='qtdePontos', ascending=False).head(5)["idCliente"])
type(top_5)

# %%
clientes

# %%
# Exemplo com "empate" de dados usuarios com o mesmo valor de salario
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)

brinquedo

# %%
# Ordena o slario e a idade, trazendo o salario do maior para o menor e a idade do menor para o maior
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])