# Módulo | Análise de dados: Aprendizado de máquina Regressão

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre penguins. A idéia é prever o peso do penguin (body_mass_g) baseado em suas características físicas e geográficas (variáveis preditivas).
'''

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

dados = sns.load_dataset('penguins')

# 2. Dados

# 2.1. Valores nulos - Trate os valores faltantes da base de dados.
dados = pd.DataFrame(dados.dropna().reset_index(drop=True))

# print(dados.info())

# 2.2. Variáveis numéricas - Identifique as variáveis numéricas e crie uma nova coluna padronizando seus valores. A nova coluna deve ter o mesmo nome da coluna original acrescida de "_std".

colunas = ['bill_length_mm', 'bill_depth_mm',
           'flipper_length_mm', 'body_mass_g']

scaler = MinMaxScaler()

for coluna in colunas:
    dados[coluna + '_std'] = scaler.fit_transform(dados[[coluna]])

# 2.3. Variáveis categóricas - Identifique as variáveis categóricas nominais e ordinais, crie uma nova coluna aplicando a técnica correta de conversão a seus valores. A nova coluna deve ter o mesmo nome da coluna original acrescida de "_nom" ou "_ord".

dados['sex_m_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Male' else 0)
dados['sex_f_nom'] = dados['sex'].apply(
    lambda sex: 1 if sex == 'Female' else 0)

species = {
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2
}
islands = {
    'Biscoe': 0,
    'Dream': 1,
    'Torgersen': 2
}

dados['species_ord'] = dados['species'].apply(
    lambda s: species[s]
)
dados['island_ord'] = dados['island'].apply(
    lambda i: islands[i]
)

# 2.4 Limpeza - Descarte as colunas originais e mantenha apenas a variável resposta e as variáveis preditivas com o sufixo _std", _nom" e "_ord".

dados.drop(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
           'flipper_length_mm', 'sex'], axis='columns', inplace=True)

# 2.5. Treino/Teste - Separe a base de dados em treino e teste utilizando uma proporção de 2/3 para treino e 1/3 para testes.

predictors_train, predictors_test, target_train, target_test = train_test_split(
    dados.drop(['body_mass_g'], axis=1),
    dados['body_mass_g'],
    test_size=0.3,
    random_state=123
)
