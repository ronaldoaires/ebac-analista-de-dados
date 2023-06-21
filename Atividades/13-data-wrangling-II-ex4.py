# Módulo | Análise de dados: Data Wrangling II

# 4. DataFrame - Utilize o dataframe brasil_df para responder as seguintes perguntas de negócio:

import pandas as pd

# Lê o arquivo CSV
brasil_df = pd.read_csv('./arquivos/13/brasil.csv', sep=';', encoding='latin_1') 

# Quais são as 10 cidades mais populosas do Brasil?
maior_populacao = brasil_df.groupby('cidade').sum()
maior_populacao = brasil_df.sort_values('populacao', ascending=False)
maior_populacao = maior_populacao[['cidade','populacao']]
print(maior_populacao[:10])

# Quais são as 5 cidades com a menor PIB per capita da região nordeste?
menor_pib = brasil_df[brasil_df['regiao'] == 'SUL']
menor_pib = menor_pib.sort_values('pib_percapita')
menor_pib = menor_pib[['cidade','pib_percapita']]
print(menor_pib[:5])

# Quais são as 15 cidades com maior PIB do estado de São Paulo?
maior_pib_sp = brasil_df[brasil_df['estado'] == 'SÃO PAULO']
maior_pib_sp = maior_pib_sp.sort_values('pib', ascending=False)
maior_pib_sp = maior_pib_sp[['cidade','pib']]
print(maior_pib_sp[:15])

# Qual é o PIB do estado de Santa Catarina?
pib_sc = brasil_df[brasil_df['estado'] == 'SANTA CATARINA'].groupby('estado').sum()
pib_sc = pib_sc[['pib']]
print(pib_sc)

# Qual é a população da região sul?
populacao_sul = brasil_df[brasil_df['regiao'] == 'SUL'].groupby('regiao').sum()
populacao_sul = populacao_sul[['populacao']]
print(populacao_sul)

# Qual é o PIB per capito médio das cidades do Mato Grosso do Sul?
pib_cidades_ms = brasil_df[brasil_df['estado'] == 'MATO GROSSO DO SUL']
pib_cidades_ms = pib_cidades_ms['pib_percapita'].mean()
print(pib_cidades_ms)

# Qual é a população do Brasil?
populacao_brasil = brasil_df['populacao'].sum()
print(f'População do Brasil: {populacao_brasil}')