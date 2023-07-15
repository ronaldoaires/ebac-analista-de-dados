# Módulo | Análise de dados: Aprendizado de máquina Classificação

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre pinguins. A ideia é prever a espécie dos pinguins baseado em suas características físicas e geográficas (variáveis preditivas).
'''

import pandas as pd
import numpy as np
import seaborn as sns
import graphviz
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

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

# 3. Modelagem
# 3.1. Treino
model = DecisionTreeClassifier()
model = model.fit(predictors_train, target_train)

# Gráfico árvore de decisão - 9 folhas
tree_data = tree.export_graphviz(model, out_file=None) 
graph = graphviz.Source(tree_data) 
graph

# 3.2. Avaliação

# Posição predita
target_predicted = model.predict(predictors_test)

# Matriz de confusão
cm = confusion_matrix(target_test, target_predicted)

# Gráfico matriz de confusão
cmd = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = model.classes_)
cmd.plot()
# A matriz mostra que o modelo acertou 100% das espécies Gentoo e Chinstrap, no entanto teve erros na classificação da espécie Adelie classificando incorretamente como Chinstrap.

# Acurácia
acuracia = accuracy_score(target_test, target_predicted)
# Imprime a acurácia formatado
print(f"Acurácia: {acuracia:.2f}%")

# 4.1. Novo penguim
novo_pinguim = np.array([
    [
        38.2, #bill_length_mm
        18.1, #bill_depth_mm,
        185.0, #flipper_length_mm,
        3950.0, #body_mass_g
        1, #sex_m_nom
        0, #sex_f_nom
        1, #biscoe_nom,
        0, #dream_nom 
        0 #torgersen_nom
    ]
])

# Faz a predição da espécie do novo pinguim utilizando o modelo treinado.
especie = model.predict(novo_pinguim.reshape(1, -1))

# Imprime a espécie predita
print(f'Espécie predita: '+ especie[0])