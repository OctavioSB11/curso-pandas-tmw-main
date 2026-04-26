# %%
import pandas as pd
import os

def read_file(file_name:str):
    # Lê o CSV, renomeia a coluna 'valor' para o nome do arquivo (tipo da taxa/dado), 
    # define 'nome' e 'período' como índices (essencial para o merge/concat lado a lado depois)
    # e remove a coluna 'cod' que não será utilizada
    df = (pd.read_csv(f"../../data/ipea/{file_name}.csv", sep=";")
            .rename(columns={"valor":file_name})
            .set_index(["nome", "período"])
            .drop(["cod"],axis=1))
    
    return df

    
# %%
# Lista todos os arquivos presentes na pasta de dados do IPEA
file_names = os.listdir("../../data/ipea/")

dfs = []
for i in file_names:
    # Separa pelo ponto e pega a primeira parte, removendo a extensão '.csv'
    file_name = i.split(".")[0]
    # Processa o arquivo com a função criada e adiciona o DataFrame resultante à lista
    dfs.append(read_file(file_name))


# Junta todos os DataFrames da lista lado a lado (axis=1).
# Como todos têm os índices 'nome' e 'período', o pandas alinha as linhas automaticamente
# Depois reseta o índice (transformando 'nome' e 'período' em colunas de volta) e ordena
df_full = (pd.concat(dfs, axis=1)
            .reset_index()
            .sort_values(["período", "nome"]))

# Exporta o resultado consolidado para um novo arquivo CSV, sem salvar o índice numérico (index=False)
df_full.to_csv("homicios_consolidado.csv", index=False, sep=";")
df_full