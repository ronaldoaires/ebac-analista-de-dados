# Módulo | Análise de dados: Aprendizado de máquina Regressão

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre penguins. A idéia é prever o peso do penguin (body_mass_g) baseado em suas características físicas e geográficas (variáveis preditivas).
'''

import pandas as pd
import seaborn as sns

dados = sns.load_dataset('penguins')

# 1.1. Analise exploratoria 

# Utilize os gráficos abaixo para entender melhor a relação entre os atributos e variável resposta da base de dados. Comente o que observou em cada gráfico.

# Atributos por sexo:
with sns.axes_style('whitegrid'):
 grafico = sns.pairplot(data=dados, hue="sex", palette="pastel")

# R: Podemos observar que a distribuição de pinguins machos e fêmeas é bem semelhante, talvez isso se deva pelo fato de os pinguins serem monogâmicos. Também podemos observar que a massa corporal das fêmeas é maior, assim como suas nadadeiras.


# Atributos por espécie:
with sns.axes_style('whitegrid'):
 grafico = sns.pairplot(data=dados, hue="species", palette="pastel")

#  R: Podemos observar que Adelie possui bico pequena e profunda, nadadeiras médias e massa corporal média. Chinstrap possui bico grande e profunda, nadadeiras médias e a espécie de menor massa corporal entre as três. Gentoo possui bico grande e de profundidade pequena, nadadeiras longas e a maior massa corporal

# Atributos por ilha:
with sns.axes_style('whitegrid'):
 grafico = sns.pairplot(data=dados, hue="island", palette="pastel")

# R: Podemos observar que a ilha Biscoe, possui a maior concentração de pinguins com a maior massa corporal, que as ilhas Biscoe e Dream tem os pinguins com as maiores nadadeiras, os maiores bicos.

