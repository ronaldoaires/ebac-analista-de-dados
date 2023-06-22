# Módulo | Análise de dados: Visualização de dados II

# 2. Correlação entre o preço do diamante com seu peso ( carat ) agrupados por sua transparêcia

import seaborn as sns

dados = sns.load_dataset("diamonds")
diamantes = dados[["price", "carat", "clarity"]]

with sns.axes_style('whitegrid'):
    grafico = sns.scatterplot(
        data=diamantes,
        x="price",
        y="carat",
        hue="clarity",
        palette="pastel"
    )
    grafico.set(
        title='Preço do diamante com seu peso',
        xlabel='Preço (USD)',
        ylabel='Peso')

    grafico.get_legend().set_title("Diamantes")

    # o gráfico mostra que quanto mais pesado é um diamante maior é o seu valor
