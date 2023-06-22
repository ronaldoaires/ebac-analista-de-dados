# Módulo | Análise de dados: Visualização de dados I

# 3. Numero de passageiros por mês entre 1949 e 1959

import seaborn as sns

dados = sns.load_dataset("flights")

voos = dados[["month", "passengers"]]
voos = dados.query("1949 <= year < 1959")

grafico = sns.barplot(
    data=voos,
    x='month',
    y='passengers',
    errorbar=None,
    palette='pastel'
)

grafico.set(title='Passageiros por mês entre 1949 e 1959',
            xlabel='Mês', ylabel='Passageiros')

# Insight

# o gráfico mostra que os meses de julho e agosto tem o maior número de passageiros
