#%%
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

dfs = pd.read_html(response.text)

uf = dfs[1]
print(uf)

#%%

uf.dtypes

#%%

# Caso for utilizar a coluna área, temos os elementos assim:  164 122,2 e queremos transformar em float

# Forma normal
numero = '164 122,2'
numero = float(numero.replace(" ", "").replace(",", "."))
numero

# %%
# Função de transformação de str pra float, utilizando os replaces para corrigir o elemento e depois transformar
def str_to_float(num: str) -> float:
    num = (num.replace(" ", "")
        .replace(",", ".")
        .replace("\xa0", "")
    )
            
    return float(num)

# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%
uf.dtypes

#%%
uf
#%%
def exp_to_anos(exp:str):
    return float(exp.replace(",", ".")
                    .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

#%%
uf

# %%
def format_percent(percent):
    percent = float(percent.replace("%", "").replace(",", "."))
    return round(percent / 100, 3)
# %%
def format_percent_1000(percent):
    percent = float(percent.replace("‰", "").replace(",", "."))
    return percent
#%%
uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(format_percent)

#%%
uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(format_percent_1000)

#%%
uf

#%%
def uf_to_regiao(uf):

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)

#%% 
uf

# %%

# Se PIB / Capita > 30.000
# +
# Mort Infantil < 15 / 1000
# +
# IDH (2010) > 700
# -> "Parece bom"

# Nao parece bom

# Navegamos linha a linha e utilizando a serie da linha para fazer as comparações
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and 
            linha["IDH (2010)"] > 700)

# %%
uf.apply(classifica_bom, axis=1)