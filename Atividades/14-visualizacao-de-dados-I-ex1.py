# Módulo | Análise de dados: Visualização de dados I

# 1. Preço do diamante por tipo de corte

import seaborn as sns

dados = sns.load_dataset('diamonds')
dados = dados[['price', 'cut']]

grafico = sns.barplot(
    data=dados,
    x='cut',
    y='price',
    errorbar=None,
    palette='pastel'
)

grafico.set(title='Preço do diamante por tipo de corte',
            xlabel='Corte', ylabel='Preço (USD)')

# Insight

# O gráfico mostra que o preço do diamente Premium tem o maior valor, enquanto que o ideal tem o menor valor
