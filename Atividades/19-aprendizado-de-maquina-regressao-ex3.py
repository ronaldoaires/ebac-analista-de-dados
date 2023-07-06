# Módulo | Análise de dados: Aprendizado de máquina Regressão

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre penguins. A idéia é prever o peso do penguin (body_mass_g) baseado em suas características físicas e geográficas (variáveis preditivas).
'''

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 2. Dados

# Carrega o conjunto de dados de pinguins
dados = sns.load_dataset('penguins')

# 2.1. Valores nulos - Tratamento de valores faltantes: remove linhas com valores faltantes e redefine os índices
dados = pd.DataFrame(dados.dropna().reset_index(drop=True))

# 2.2. Variáveis numéricas - Padronização das variáveis numéricas
colunas = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
for coluna in colunas:
    media = dados[coluna].mean()
    desvio_padrao = dados[coluna].std()
    dados[coluna + '_std'] = (dados[coluna] - media) / desvio_padrao

# 2.3. Variáveis categóricas - Conversão das variáveis categóricas nominais e ordinais
dados['sex_m_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Male' else 0)
dados['sex_f_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Female' else 0)

dados['adelie_nom'] = dados['species'].apply(lambda s: 1 if s == 'Adelie' else 0)
dados['chinstrap_nom'] = dados['species'].apply(lambda s: 1 if s == 'Chinstrap' else 0)
dados['gentoo_nom'] = dados['species'].apply(lambda s: 1 if s == 'Gentoo' else 0)

dados['biscoe_nom'] = dados['island'].apply(lambda i: 1 if i == 'Biscoe' else 0)
dados['dream_nom'] = dados['island'].apply(lambda i: 1 if i == 'Dream' else 0)
dados['torgersen_nom'] = dados['island'].apply(lambda i: 1 if i == 'Torgersen' else 0)

# 2.4. Limpeza - Descarta colunas originais, mantendo apenas as variáveis preditivas e a variável resposta
pinguins = dados.drop(['sex', 'species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'], axis=1)

# 2.5. Treino/Teste - Separação dos dados em treino e teste utilizando proporção de 2/3 para treino e 1/3 para teste
predictors_train, predictors_test, target_train, target_test = train_test_split(
    pinguins.drop(['body_mass_g'], axis=1),
    pinguins['body_mass_g'],
    test_size=0.33,
    random_state=123
)

# 3. Modelagem

# 3.1. Treino - Modelo de regressão linear

# Criação e treinamento do modelo de regressão linear
model = LinearRegression()
modelo = model.fit(predictors_train, target_train)

# Predição do conjunto de teste
target_predicted = model.predict(predictors_test)

# 3.2. Avaliação - Cálculo do erro quadrático médio (RMSE)
rmse = np.sqrt(mean_squared_error(target_test, target_predicted))
# Imprime o valor do rmse formatado
print(f'RMSE: {rmse:.2f}g')

# 4. Predição - Peso predito para novo pinguim

# Valores padronizados para as características do novo pinguim
bill_length_mm_std = (
    38.2 - dados['bill_length_mm'].mean()) / dados['bill_length_mm'].std()

bill_depth_mm_std = (
    18.1 - dados['bill_depth_mm'].mean()) / dados['bill_depth_mm'].std()

flipper_length_mm_std = (
    185.0 - dados['flipper_length_mm'].mean()) / dados['flipper_length_mm'].std()

# 4.1. Novo penguim
novo_pinguim = np.array([
    [
        bill_length_mm_std,
        bill_depth_mm_std,
        flipper_length_mm_std,
        1, # sex_m_nom
        0, # sex_f_nom
        1, # adelie_nom
        0, # chinstrap_nom 
        0, # gentoo_nom 
        1, # biscoe_nom 
        0, # dream_nom 
        0 # torgersen_nom
    ]
])

# Faz a predição do peso do novo pinguim utilizando o modelo treinado.
peso_predito = model.predict(novo_pinguim.reshape(1, -1))
# Formata o valor predito
peso = list(map('{:.2f}kg'.format,peso_predito))
# Imprime o valor predito do peso do novo pinguim.
print(f'Peso predito: ' + peso[0])