# Módulo | Análise de dados: Aprendizado de máquina Classificação

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre pinguins. A ideia é prever a espécie dos pinguins baseado em suas características físicas e geográficas (variáveis preditivas).
'''

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

# Carrega o conjunto de dados de pinguins
dados = sns.load_dataset('penguins')

# 2. Dados
# 2.1. Valores nulos - Tratamento de valores faltantes: remove linhas com valores faltantes e redefine os índices
dados = pd.DataFrame(dados.dropna().reset_index(drop=True))

# 2.2. Variáveis categóricas - Conversão das variáveis categóricas nominais e ordinais
dados['sex_m_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Male' else 0)
dados['sex_f_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Female' else 0)

dados['biscoe_nom'] = dados['island'].apply(lambda i: 1 if i == 'Biscoe' else 0)
dados['dream_nom'] = dados['island'].apply(lambda i: 1 if i == 'Dream' else 0)
dados['torgersen_nom'] = dados['island'].apply(lambda i: 1 if i == 'Torgersen' else 0)

# 2.3. Limpeza - Descarta colunas originais, mantendo apenas as variáveis preditivas e a variável resposta
pinguins = dados.drop(['sex', 'island'], axis=1)

# 2.4. Treino/Teste - Separação dos dados em treino e teste utilizando proporção de 2/3 para treino e 1/3 para teste
predictors_train, predictors_test, target_train, target_test = train_test_split(
    pinguins.drop(['species'], axis=1),
    pinguins['species'],
    test_size=0.30,
    random_state=123
)
