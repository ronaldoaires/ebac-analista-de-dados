# Módulo | Análise de dados: Aprendizado de máquina Classificação

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre penguins. A ideia é prever a (species) baseado em suas características físicas e geográficas (variáveis preditivas).
'''

import seaborn as sns

dados = sns.load_dataset('penguins')

# 1. Análise exploratória

# Utilize os gráficos indicados no material de apoio para entender melhor a relação entre os atributos e variável resposta da base de dados. Comente o que observou em cada gráfico.

# Atributos numéricos por espécie
with sns.axes_style('whitegrid'):
  grafico = sns.pairplot(data=dados.drop(['sex', 'island'], axis=1), hue="species", palette="pastel")

# R: Existem mais pinguins da espécie Adelie, seguido da espécie Gentoo e Chinstrap. 

# Sexo por espécie
with sns.axes_style('whitegrid'):
  grafico2 = sns.countplot(data=dados, x='sex', hue="species", palette="pastel")

#  R: Podemos observar que a distribuição de pinguins machos e fêmeas é bem semelhante, talvez isso se deva pelo fato de os pinguins serem monogâmicos.

# Ilha por espécie
with sns.axes_style('whitegrid'):
  grafico = sns.countplot(data=dados, x='island', hue="species", palette="pastel")

# R: A espécie Adelie é encontrado nas 3 ilhas, já a espécie Chinstrap é encontrada somente na ilha Dream e, por fim, a espécie Gentoo somente na ilha Biscoe.

