# Módulo | Análise de Dados: Séries Temporais

'''
1. Correlação entre consumo de energia elétrica e temperatura

Neste código, vamos correlacionar a base de dados de consumo de energia elétrica com uma base de dados de temperatura média das tres maiores cidades do sudeste: São Paulo, Rio de Janeiro e Belo Horizonte.
'''

# Importando as bibliotecas
import numpy as np
import pandas as pd
import seaborn as sns

# 1.1. Energia

# Carregando os dados
energia = pd.read_csv('./arquivos/22/energia.csv', sep=';', parse_dates=[0])

'''
Responda:

Qual é a granularidade da base de dados: ?
R: Mensal

Qual é o intervalo de tempo (min/max): ?
energia['referencia'].min()
energia['referencia'].max()

R: 01/01/2004 até 01/12/2020

'''

# 1.2. Temperatura

# Carregando os dados
temperatura = pd.read_csv(
    './arquivos/22/temperatura.csv', sep=';', parse_dates=[0])

'''
Responda:

Qual é a granularidade da base de dados: ?
R: Diária

Qual é o intervalo de tempo (min/max): ?

R: 15/07/2018 até 31/12/2018

'''
# 2. Processamento

# 2.1. Energia

#  Atribui ao index a coluna temporal
energia = energia.set_index('referencia')

# Seleciona apenas os dados entre 2019 e 2020
energia = energia['2019':'2020']
# energia.shape - (24, 3)

# 2.2. Temperatura

#  Atribui ao index a coluna temporal
temperatura = temperatura.set_index('referencia')

# Seleciona apenas os dados entre 2019 e 2020
temperatura = temperatura['2019':'2020']
# temperatura.shape - (731, 3)

# Remove todas as linhas que apresentem pelo menos um valores nulo.
temperatura = temperatura.dropna()
temperatura.isnull().sum()

# Combina as três colunas de temperatura em uma só chamada de temp-media e agrega pela média (obtendo assim uma temperatura média aproximada da região sudeste).
temperatura['temp-media'] = temperatura.mean(axis=1)

# Reamostra o dataframe para que sua granularidade seja a mesma dos dados de consumo de energia elétrica, utilizando a média como métrica de agregação.
temperatura_mensal = temperatura.resample(rule='1m').mean()
# temperatura_mensal.shape - (24, 4)

# 3. Correlação

# 3.1. Consumo residencial

# Gera um gráfico de linha para a série temporal de temperatura média agregada temp-media.
sns.set_style("whitegrid")

grafico_temperatura = sns.lineplot(
    data=temperatura_mensal['temp-media'],
    marker="."
)
grafico_temperatura.set(
    title='Temperatura Média',
    xlabel='Data',
    ylabel='Temperatura'
)
grafico_temperatura.figure.set_size_inches(10, 5)

# Gera um gráfico de linha para a série temporal do consumo de energia residencial.
grafico_energia_residencial = sns.lineplot(
    data=energia['residencial'],
    marker='.'
)
grafico_energia_residencial.set(
    title='Consumo Energia Residêncial',
    xlabel='Data',
    ylabel='Consumo (MWh)'
)
grafico_energia_residencial.figure.set_size_inches(10, 3)

#  Utiliza o método corrcoef do pacote Numpy para calcular o coeficiente de Pearson entre o consumo de energia elétrica residencial e a temperatura média agregada temp-media.
correlacao = np.corrcoef(temperatura_mensal['temp-media'], energia['residencial'])
print(correlacao)

'''
A temperatura é um bom atributo para prever o consumo de energia elétrica residencial?

R: Sim, a temperatura está correlacionada ao consumo de energia, o consumo aumenta no verão e diminui no inverno.
'''

# 3.2. Consumo comercial

# Gera um gráfico de linha para a série temporal de temperatura média agregada temp-media.

grafico_temperatura_comercial = sns.lineplot(
    data=temperatura_mensal['temp-media'],
    marker="."
)
grafico_temperatura_comercial.set(
    title='Temperatura Média',
    xlabel='Data',
    ylabel='Temperatura'
)
grafico_temperatura_comercial.figure.set_size_inches(10, 5)

# Gera um gráfico de linha para a série temporal do consumo de energia comercial.
grafico_energia_comercial = sns.lineplot(
    data=energia['comercial'],
    marker='.'
)
grafico_energia_comercial.set(
    title='Consumo Energia Comercial',
    xlabel='Data',
    ylabel='Consumo (MWh)'
)
grafico_energia_comercial.figure.set_size_inches(10, 3)

#  Utiliza o método corrcoef do pacote Numpy para calcular o coeficiente de Pearson entre o consumo de energia elétrica comercial e a temperatura média agregada temp-media.
correlacao = np.corrcoef(temperatura_mensal['temp-media'], energia['comercial'])
print(correlacao)
'''
A temperatura é um bom atributo para prever o consumo de energia elétrica comercial?

R: Sim, a temperatura está correlacionada ao consumo de energia, o consumo aumenta no verão e diminui no inverno.
'''

# 3.3. Consumo industrial
# Gera um gráfico de linha para a série temporal de temperatura média agregada temp-media.

grafico_temperatura_industrial = sns.lineplot(
    data=temperatura_mensal['temp-media'],
    marker="."
)
grafico_temperatura_industrial.set(
    title='Temperatura Média',
    xlabel='Data',
    ylabel='Temperatura'
)
grafico_temperatura_industrial.figure.set_size_inches(10, 5)

# Gera um gráfico de linha para a série temporal do consumo de energia industrial.
grafico_energia_industrial = sns.lineplot(
    data=energia['industrial'],
    marker='.'
)
grafico_energia_industrial.set(
    title='Consumo Energia Industrial',
    xlabel='Data',
    ylabel='Consumo (MWh)'
)
grafico_energia_industrial.figure.set_size_inches(10, 3)

#  Utiliza o método corrcoef do pacote Numpy para calcular o coeficiente de Pearson entre o consumo de energia elétrica industrial e a temperatura média agregada temp-media.
correlacao = np.corrcoef(temperatura_mensal['temp-media'], energia['industrial'])
print(correlacao)
'''
A temperatura é um bom atributo para prever o consumo de energia elétrica industrial?

R: Sim, a temperatura está correlacionada ao consumo de energia, o consumo aumenta no verão e diminui no inverno.
'''