# Módulo | Análise de dados: Visualização de dados I

# 2. Número de passageiros em dezembro por ano

import seaborn as sns

dados = sns.load_dataset('flights')

voos = dados.query("month=='Dec'")

with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(
        data=voos, 
        x="year",
        y="passengers",
        palette="pastel"
    )

    grafico.set(title='Passageiros em dezembro por ano',
                xlabel='Ano', ylabel='Passageiros')

# Insight

# O gráfico mostra que o número de passareigos ao longo dos anos em dezembro tem um crescimento constante
