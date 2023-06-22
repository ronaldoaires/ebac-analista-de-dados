# Módulo | Análise de dados: Visualização de dados II

# 1. Preços outliers de diamante

import seaborn as sns

dados = sns.load_dataset("diamonds")

with sns.axes_style('whitegrid'):
    grafico = sns.boxplot(x=dados["price"])
    grafico.set(title='Preço dos diamantes', xlabel='Preço')


# o gráfico mostra que a concentração dos preços dos diamantes está entre 2mil e 55mil e que raramente passa dos 125mil
