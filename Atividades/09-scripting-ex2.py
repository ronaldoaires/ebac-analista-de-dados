# Módulo | Python: Scripting

# 2. Script de Visualização - script para gerar um grafico da taxa CDI do site da B3

# importando pacotes
import pandas as pd
import seaborn as sns

# Extraindo as colunas hora e taxa
df = pd.read_csv('./arquivos/09/taxa-cdi.csv')

# Salvando gráfico
grafico = sns.lineplot(
    x=df['hora'],
    y=df['taxa']
)
_ = grafico.set_xticklabels(
    labels=df['hora'],
    rotation=90
)

grafico.get_figure().savefig("./arquivos/09/cdi.png")
