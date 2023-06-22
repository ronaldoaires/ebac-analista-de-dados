# Módulo | Análise de dados: Visualização de dados II

# 3. Distribuição contínua aproximada do peso ( weight ) de carros

import seaborn as sns

dados = sns.load_dataset("mpg")
carros = dados[["weight"]]

with sns.axes_style('whitegrid'):
    grafico = sns.histplot(
        data=carros,
        x="weight",
        kde=True
    )
    grafico.set(
        title='Peso dos carros',
        xlabel='Peso',
        ylabel='Contagem'
    )

    # o gráfico mostra que a maior parte dos carros pesa por volta de 2mil KG e vai caindo de peso
